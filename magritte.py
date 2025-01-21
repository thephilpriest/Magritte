#!/usr/bin/python3

'''
Copyright 2024, 2025 Philip S. Priest

This file is part of Magritte.

Magritte is free software: you can redistribute it and/or modify it under the terms of the GNU General Public 
License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any 
later version.
Magritte is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied
warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License for more
details.
You should have received a copy of the GNU General Public License along with Magritte. If not, 
see <https://www.gnu.org/licenses/>.
'''

import smidgeon
import pipe

 
if __name__ == '__main__':
    # All of this will eventually come from the user, 
    # That which makes a pipe
    pipe_params = {
        'max_allowed_velocity' : 28 # Presuming that all distances are measured in MM, this equates to 100KPH
    }
    # This is the number of *virtual* milliseconds between each wake-up
    wake_interval = 50
    # This is the number of *virtual* milliseconds the simulation will run for
    run_time = 3600000 # That's 1 hour
    # This is the target following distance in MS (*NOT* MM); augmented by a smidgeon's tailgatiness and erraticness values
    ideal_following_distance = 2000
    # That which makes a smidgeon
    new_smidgeon_params = {
        'mean_length' : 4575,
        'std_dev_length' : 750,
        'mean_max_velocity' : 55,
        'std_dev_max_velocity' : 5,
        'mean_max_acceleration' : 7,
        'std_dev_max_acceleration' : 1,
        'mean_max_deceleration' : 15, # PSP fact check this
        'std_dev_max_deceleration' : 2,
        'mean_acceleratiness' : 50,
        'std_dev_acceleratiness' : 25,
        'mean_deceleratiness' : 50,
        'std_dev_deceleratiness' : 25,
        'mean_tailgatiness' : 50,
        'std_dev_tailgatiness' : 25,
        'mean_speederiness' : 50,
        'std_dev_speederiness' : 25,
        'mean_patience' : 50,
        'std_dev_patience' : 15,
        'mean_erraticness' : 15,
        'std_dev_erraticness' : 25,
        'intl_velocity' : 28, # PSP I am for now opting to inject new smidgeons at the exact speed limit
        'intl_inst_acceleration' : 0, # PSP I am for now opting to inject new smidgeons free of acceleration or deceleration
        'mean_reaction_time' : 250,
        'std_dev_reaction_time' : 50
    }

    # Stuff not coming from the user
    # The current number of elapsed *virtual* milliseconds
    current_time = 0
    # The smidgeon that will complete entry into the pipe next
    # We need to always have one on hand (done within the main loop) so that we can 
    # append it when the distance and tailgating requirements are satisfied, the latter of which is
    # a notion that is distinct to each smidgeon when it is born
    entrant_smidgeon = None
    # Did the *virtual* millisecond from when the last wake_interval ended include an incomplete smidgeon append (this could be
    # the case if wake_interval is lower than the minimum possible smidgeon length)
    actively_appending = False
    # This instantiates the pipe.
    plumbum = pipe.pipe(pipe_params)
  
    # THE MAIN LOOP
    while current_time < run_time:
        # Do we have an entrant smidgeon? If not, make one - you must have on at the beginning of every cycle - even if it's not ready to be added to the pipe yet
        if entrant_smidgeon is None:
            entrant_smidgeon = smidgeon.smidgeon(new_smidgeon_params)
            qty_appended = 0
            # Until we know how much of entrant_smidgeon to append to plumbum.current_layout in this cycle, we will set it to 0 
            qty_to_append = 0
        # If this is the *virtual* millisecond of inception, then we MUST be actively appending a smidgeon since position 0 of plumbum.current_layout
        # must always be the tip of the 1st smidgeon in the pipe
        if current_time == 0:
            actively_appending = True
        # If entrant_smidgeon is clear to begin appending (the distance from the tail of plumbum.current_layout to the last smidgeon is "okay"), then
        # we can set actively_appending to True
        if actively_appending == False and (len(plumbum.current_layout)-1) - plumbum.get_end_of_last_smidgeon() >= (
            entrant_smidgeon.get_inst_min_okay_follow_distance(ideal_following_distance * plumbum.velocity_limit)):
            actively_appending = True
            print(f"Flipped actively_appending to {actively_appending} at {current_time}") #PSP
        # Are we actively appending during this *virtual* millisecond
        if actively_appending == True:
            qty_to_append = min ((entrant_smidgeon.length-qty_appended), (wake_interval * plumbum.velocity_limit)) #This needs to take velocity into account PSP
            plumbum.add_a_smidgeon(entrant_smidgeon, qty_to_append)
            qty_appended += qty_to_append
            if qty_appended == entrant_smidgeon.length:
                actively_appending = False
                print(f"Flipped actively_appending to {actively_appending} at {current_time}") #PSP
                entrant_smidgeon = None
        # append up to wake_interval vacant space into plumbum.current_layout, depending on how many units we added with add_a_smidgeon
        if (wake_interval - qty_to_append) > 0:
            plumbum.add_vacant_space((wake_interval - qty_to_append))

        # go through all the smidgeons and do their reactive()
            for smidgeon_id in plumbum.all_the_smidgeons.keys():
                if plumbum.all_the_smidgeons[smidgeon_id].reactive(wake_interval) is True:
                    print(f"smidgeon {smidgeon_id} is reactive") #PSP

            # any smidgeon that is reactive will do a set_intention()
        # if the time is right inject and dick move in the form of a really nasty intention
            # make it persist somehow...
            # release it when done?
            # Which smidgeon is the dick?
            # from the README
            # The interruptions can be slow-downs or stops and need to be described in terms that assert: the rate of the slowdown,
            # the duration of the slowdown, the rate of the speed-back-up and the speed both before and after the event
        # go through all the smidgeons and execute their intentions
            # This will be done via pipe.execute_intentions()
        current_time += wake_interval