#!/usr/bin/env python3
'''
Module 6: type-annotated func sum_mixed_list takes mxd_lst param
of int and float and return sum as float
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''
    function takes mxd_list as param and returns sum of list as float
    '''
    return sum(mxd_lst)
