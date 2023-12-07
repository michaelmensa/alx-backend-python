#!/usr/bin/env python3
'''
Module 8: type-annotated func make_multiplier that takes a multiplier
float as param and returns a function that multiplies a float by multiplier
'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''
    function that returns a function that multiplies a float by multiplier
    '''
    def multiplier_function(x: float) -> float:
        '''
        function that is going to be called by the make_multiplier funciton
        '''
        return x * multiplier
    return multiplier_function
