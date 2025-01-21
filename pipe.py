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

class pipe:
    def __init__(self, params: dict):
        # A dict of every smidgeon keyed by their unq_id values.
        self.all_the_smidgeons = {}
        # The prescribed "speed limit" of the pipe; the distance covered per *virtual* millisecond (IE, 1/nth of
        # the wake interval). The unit is arbitrary but not weird in that it is all base 10 and not the BS miles
        # and feet stuff. but my use cases treat it as MM
        # It is important to know that this limit is not hard-and-fast, smidgeons can be speeders.
        self.velocity_limit = params['max_allowed_velocity']
        # The current layout of the pipe, a list where position 0 is the tip of the 1st smidgeon and each 
        # position represents some atomic unit of length where unconsumed space is None and consumed spaces 
        # are filled with smidgeon.unq_id values
        self.current_layout = []

    def get_end_of_last_smidgeon(self) -> int:
        '''
        This method will return the position self.current_layout holding the last segment of the last smidgeon
        '''
        descender = len(self.current_layout) - 1
        while descender > 0:
            if self.current_layout[descender] is not None:
                return descender
            descender -= 1
        return descender


    def add_a_smidgeon(self, el_smidge: smidgeon, fragment: int):
        '''
        This method will append a smidgeon to the end of the pipe
        '''
        
        self.all_the_smidgeons[el_smidge.unq_id] = el_smidge
        measured = 0
        while measured < fragment :
            self.current_layout.append(el_smidge.unq_id)
            measured += 1

    def add_vacant_space(self, amount: int):
        '''
        This method will add `amount` empty spaces to the end of the pipe
        '''

        added = 0
        while added < amount:
            self.current_layout.append(None)
            added += 1

    def execute_intentions(self):
        '''
        This will also clear the intention value for each smidgeon
        '''
        pass