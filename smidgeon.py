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

import uuid
import numpy
import pipe

class smidgeon:

    def __init__(self, params: dict):
        #Unique ID for the smidgeon at hand
        self.unq_id = uuid.uuid4()
        print(f"I made {self.unq_id}") #PSP
        # Numpy style selfs
        # How long is this smidgeon object "bumper to bumper"
        self.length = int(numpy.random.default_rng().normal(params['mean_length'], params['std_dev_length']))
        # Maximum rate of travel
        self.max_velocity = int(numpy.random.default_rng().normal(params['mean_max_velocity'], params['std_dev_max_velocity']))
        # Maximum rate of acceleration
        self.max_acceleration = int(numpy.random.default_rng().normal(params['mean_max_acceleration'], params['std_dev_max_acceleration']))
        # Maximum rate of deceleration
        self.max_deceleration = int(numpy.random.default_rng().normal(params['mean_max_deceleration'], params['std_dev_max_deceleration']))
        # Willingness to accelerate at the maximum rate
        self.acceleratiness = int(numpy.random.default_rng().normal(params['mean_acceleratiness'], params['std_dev_acceleratiness']))
        # Willingness to decelerate at the maximum rate
        self.deceleratiness = int(numpy.random.default_rng().normal(params['mean_deceleratiness'], params['std_dev_deceleratiness']))
        # Willingness to follow the smidgeon ahead of it closely
        self.tailgatiness = int(numpy.random.default_rng().normal(params['mean_tailgatiness'], params['std_dev_tailgatiness']))
        # Willingness to travel at a rate that exceeds the limit for the pipe
        self.speederiness = int(numpy.random.default_rng().normal(params['mean_speederiness'], params['std_dev_speederiness']))
        # More impatient smidgeons may close the gap as smidgeons several units ahead of them start advancing in anticipation of the smidgeon immediately in front of them advancing
        self.patience = int(numpy.random.default_rng().normal(params['mean_patience'], params['std_dev_patience']))
        # How rigidly does this smidgeon adhere to the "iness" and patience parameters
        self.erraticness = int(numpy.random.default_rng().normal(params['mean_erraticness'], params['std_dev_erraticness']))
        # The average time between set_intention() executions
        self.mean_reaction_time = params['mean_reaction_time']
        # The standard_deviation from the mean for time between set_intention() executions
        self.std_dev_reaction_time = params['std_dev_reaction_time']
        # How long until the next opportunity to run set_intention()
        self.reaction_count_downer = int(numpy.random.default_rng().normal(self.mean_reaction_time, self.std_dev_reaction_time))
        # Directly assigned selfs
        # Current rate of travel
        self.cur_velocity = params['intl_velocity']
        # Current rate of acceleration; positive for accelerating, negative for decelerating
        self.inst_acceleration = params['intl_inst_acceleration']
        # is this just accelerate/decelerate or is it accomplish-a-certain-goal? I feel like the goal is dynamic and changes iteration to iteration; that should be a function of the "iness" values and maybe be augmented by a value for eraticness (how rigidly does the smidgeon adhere to its "iness" values.
        self.intention = None

    def reactive(self, time_gone_by: int) -> bool:
        '''
        This method takes the number of *virtual* milliseconds since we last checked to see if this smidgeon could react
        and decrements the counter, if we hit or go below zero then reaction is allowed so return True *AND* reset the 
        counter to a new value. If we do not hit or go below zero then return False since we cannot react yet.
        '''
        if self.reaction_count_downer <= time_gone_by:
            self.reaction_count_downer = int(numpy.random.default_rng().normal(self.mean_reaction_time, self.std_dev_reaction_time))
            return True
        else:
            self.reaction_count_downer -= time_gone_by
            return False


    def set_intention(self, the_pipe: pipe, my_tip: int):
        '''
        This method takes the pipe and the forward-most position in the pipe that this smidgeon occupies
        It looks minimally at the one immediately in front of it reviewing its velocity, instantaneous
        acceleration and distance from self to determine what action self should take during the action
        phase; IE, the intention.
        '''
        # Where is this smidgeon in the pipe?
        # What is ahead of me?