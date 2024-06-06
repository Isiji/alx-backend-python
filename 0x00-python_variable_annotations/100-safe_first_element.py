#!/usr/bin/python3
'''Safe first element module
'''
from typing import Sequence, Union, Any

def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Returns the first element of a sequence.
    '''
    if lst:
        return lst[0]
    else:
        return None