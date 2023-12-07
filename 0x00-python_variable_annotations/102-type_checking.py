#!/usr/bin/env python3
'''
Module 12: validating this func with mypy and applying the
necessary changes
'''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''
    using mypy with my head before using mypy.
    '''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = tuple([12, 72, 91])

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, int(3.0))
