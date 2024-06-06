#!/usr/bin/python3

from typing import Tuple, List

def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Returns a list of tuples.
    '''
    zoomed_in: List[Tuple] = [
        (i * factor) for i in lst
    ]
    return zoomed_in