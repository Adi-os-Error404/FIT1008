""" 
Examples of documentation used in FIT1008/FIT1054/FIT2085.

This module demonstrates the level of documentation for modules and
functions that we will require in the unit. Examples for classes,
exceptions and testing will appear later in the unit.

Further to Further examplanation of good documentation under Important 
Documents on Moodle for more details.
"""

__author__ = "Maria Garcia de la Banda"

from typing import List, Union, TypeVar  # this is how we import things
T = TypeVar('T')


def max_age(age1: int, age2: int) -> int:
    return age1 if age1 > age2 else age2


def has_a_negative(list: List[int]) -> bool:
    """ Checks if the list has a negative number.

    :pre: The list must contain elements
    :post: The list should not be modified
    :complexity: Best O(1) if negative number appears first, worst O(N),
                 where N is the length of list, when all are >= 0
    """
    assert len(list) > 0, "List must contain elements"
    
    for item in list:
        if item < 0:
            return True
    return False


def string_to_number(string: str) -> Union[int, float]:
    """ Converts a string into an int or a float.
    :raises ValueError: if the string is neither an int nor a float
    """
    try:
        return int(string)
    except ValueError:
        return float(string)



def disjoint(list1: List[T], list2: List[T]) -> bool:
    """ Checks if two lists have no elements in common.

    :param arg1: often student in a Monash Activiity (lecture, lab, etc)
    :param arg2: often students in a different Monash Activiity 
    :complexity: Best O(1) if their first element is the same, worst 
                 O(N1*N2)*O(==), where NX is the length of listX, and 
                 O(==) is the complexity of ==, when they are disjoint
    """
    for item1 in list1:
        for item2 in list2:
            if item1 == item2:
                return False
    return True  


def main():
    """ Calls all functions with some inputs and prints the result."""
    print(max_age(-1, 3)) 
    print(max_age(-1, -1))
    print(has_a_negative([1, 2, 3, -4]))
    print(has_a_negative([]))
    print(string_to_number("  14  "))
    print(string_to_number("  -14.6  "))
    print(disjoint([1, 2, 3],[1]))
    print(disjoint([1, 2, 3],[4, 5, 6, 7]))
    print(string_to_number("  1  2  "))   # should throw ValueError

if __name__ == "__main__":
    main()
