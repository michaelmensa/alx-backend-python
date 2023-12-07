#!/usr/bin/env python3
'''
Module 9: Annotate the func params and return values with appropriate types
'''
from typing import Iterable, List, Tuple, Sequence


'''
def element_length(lst):
    return [(i, len(i)) for i in lst]
'''


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''
    type annotated function of the given function above
    '''
    return [(i, len(i)) for i in lst]
