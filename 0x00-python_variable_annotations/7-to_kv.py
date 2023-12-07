#!/usr/bin/env python3
'''
Module 7: type-annotated func to_kv takes a str k and int || float v as params
and returns a tuple. first param of tuple is str k, second element of tuple is
square of int/float v should be annotated as float
'''

from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''
    function takes k(str) and v(int || float) and returns tuple(str, float)
    '''
    t = v**2
    return (k, t)
