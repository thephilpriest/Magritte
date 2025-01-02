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
    #Get all the params from the user
    #Start the clock at T=0
    #as the clock advances, add more elements to pipe.current_layout
    #add new smidgeons when the params line up for it
    
    #This will eventually from the the user
    pipe_params = {'max_allowed_velocity' : 50}    
    cest = pipe.pipe(pipe_params)
    #These will eventually come from the user
    launch_vals = {
        'mean_length' : 100,
        'std_dev_length' : 10,
        'mean_max_velocity' : 80,
        'std_dev_max_velocity' : 7,
        'mean_max_acceleration' : 10,
        'std_dev_max_acceleration' : 1,
        'mean_max_deceleration' : 15,
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
        'std_dev_patience' : 25,
        'mean_erraticness' : 50,
        'std_dev_erraticness' : 25,
        'intl_velocity' : 50,
        'intl_inst_acceleration' : 5
        }
    smidge = smidgeon.smidgeon(launch_vals)
    cest.add_a_smidgeon(smidge)
    print(len(cest.current_layout))
    # The idea here is that we wake up periodically and add some (possibly 0) vacant space
    cest.add_vacant_space()
    
    
#Essentially, i think that we want to take multiple passes per time slice.
#the first pass each smidgeon evaluates the situation ahead of it and asserts its intentions
#the second pass all the smidgeons execute their intentions

#when we inject new items into the pipe are they all identical?
#are there ranges for each parameter?
#are there standard deviations for each parameter?
#Do we begin with an empty pipe?
#what controls the autonomous-ness of the smidgeons


#f len(self.current_layout) > 0:
            #Figure out how far back to put the next smidgeon
            #if we are at max tailgatiness then there will be 0 gap
            #This needs to be based upon what metric we use for tailgating 
            #Perhaps this code should reject this if the tailgatiness is violated