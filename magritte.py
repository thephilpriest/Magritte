#!/usr/bin/python3

import uuid
import numpy

class smidgeon:

    def __init__(self, params: dict):
        self.unq_id = uuid.uuid4()
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
        # Willingness to travel at a rate that exceeds to limit for the pipe
        self.speederiness = int(numpy.random.default_rng().normal(params['mean_speederiness'], params['std_dev_speederiness']))
        # More impatient smidgeons may close the gap as smidgeons several units ahead of them start advancing in anticipation of the smidgeon immediately in front of them advancing
        self.patience = int(numpy.random.default_rng().normal(params['mean_patience'], params['std_dev_patience']))
        # How rigidly does this smidgeon adhere to the "iness" and patience parameters
        self.erraticness = int(numpy.random.default_rng().normal(params['mean_erraticness'], params['std_dev_erraticness']))

        # Directly assigned selfs
        # Current rate of travel
        self.cur_velocity = params['intl_vel']
        # Current rate of acceleration; positive for accelerating, negative for decelerating
        self.inst_celeration = params['intl_acc']
        # is this just accelerate/decelerate or is it accomplish a certain goal? I feel like the goal is dynamic and changes iteration to iteration; that should be a function of the "iness" values and maybe be augmented by a value for eraticness (how rigidly does the smidgeon adhere to its "iness" values.
        self.intention = None
        
    
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
