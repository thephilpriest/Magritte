#!/usr/bin/python3

import uuid

class smidgeon:

    def __init__(self, params: dict):
        self.unq_id = uuid.uuid4()
        self.length = params['length'] # How long is this smidgeon object "bumper to bumper"
        self.cur_velocity = params['intl_vel'] # Current rate of travel
        self.max_velocity = params['max_vel'] # Maximum rate of travel
        self.max_acceleration = params['max_acc'] # Maximum rate of acceleration
        self.max_decceleration = params['max_dec'] # Maximum rate of deceleration
        self.inst_celeration = params['intl_acc'] # Current rate of acceleration; positive for accelerating, negative for decelerating
        self.acceleratiness = params[''] # Willingness to accelerate at the maximum rate
        self.deceleratiness = params[''] # Willingness to decelerate at the maximum rate
        self.tailgatiness = params [''] # Willingness to follow the smidgeon ahead of it closely
        self.speederiness = params[''] # Willingness to travel at a rate that exceeds to limit for the pipe
        self.patience = params[''] # more impatient smidgeons may close the gap as smidgeons several units ahead of them start advancing in anticipation of the smidgeon immediately in front of them advancing
        self.erraticness = params[''] # How rigidly does this smidgeon adhere to the "iness" and patience parameters
        self.intention = params[''] # is this just accelerate/decelerate or is it accomplish a certain goal? I feel like the goal is dynamic and changes iteration to iteration; that should be a function of the "iness" values and maybe be augmented by a value for eraticness (how rigidly does the smidgeon adhere to its "iness" values.
        
    
#class pipe:

#Essentially, i think that we want to take multiple passes per time slice.
#the first passs each smidgeon evaluates the situation ahead of it and asserts its intentions
#the second pass all the smidgeons execute their intentions

#when we inject new items into the pipe are they all identical?
#are there ranges for each parameter?
#are there standard devaitions for each parameter?
#Do we begin with an empty pipe?
#what controls the autonomous-ness of the smidgeons
#i think nthat would be 0 eraticness and them all being identical
