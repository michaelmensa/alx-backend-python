#!/usr/bin/env python3
'''
Module 5: type-annotated func sum_list which takes a list input_list
of floats as param and returns their sum as a float
'''


from typing import List


def sum_list(input_list: List[float]) -> float:
    '''
    function that takes a list of float and returns the sum.
    '''
    return sum(input_list)
