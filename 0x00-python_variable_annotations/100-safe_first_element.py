#!/usr/bin/env python3
'''
Module 10: More duck typing. If it quacks like a duck, swims like a duck,
walks like a duck, it is probably a duck.
'''
from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''
    function to augment with type-annotations.
    '''
    if lst:
        return lst[0]
    else:
        return None
