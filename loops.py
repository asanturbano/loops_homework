"""
Complete the code to pass all the test
"""

#####################################################################
# For Loops


def print_list(lst):
    """Prints out each item in a list.

    >>> lst = ["ant", "bear", "caterpillar"]
    >>> print_list(lst)
    ant
    bear
    caterpillar
    """

    # ADD YOUR CODE HERE
    for item in lst:
        print item


def print_even_0_to_20():
    """Prints out only the even numbers from 0 to 20.

    >>> print_even_0_to_20()
    0
    2
    4
    6
    8
    10
    12
    14
    16
    18
    20
    """

    # ADD YOUR CODE HERE
    for item in range(0,22,2):
        print item


#####################################################################
# While Loops

def count_down_20():
    """Uses a while loop and prints from 20 to 0.

    >>> count_down_20()
    20
    19
    18
    17
    16
    15
    14
    13
    12
    11
    10
    9
    8
    7
    6
    5
    4
    3
    2
    1
    """

    count = 20

    # ADD YOUR CODE HERE
    for item in range(20,0,-1):
        print item


#####################################################################
# Don't touch the code below!
# This is just allowing us to run the doctests

if __name__ == '__main__':
    import doctest
    if doctest.testmod().failed == 0:
        print "\n*** ALL TESTS PASSED. AWESOME WORK!\n"
