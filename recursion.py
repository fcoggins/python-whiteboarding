def powers_of_two(n):
    '''Recursive solution to calculate 2**n

    >>> powers_of_two(0)
    1
    >>> powers_of_two(1)
    2
    >>> powers_of_two(4)
    16

    '''

    if n == 0:
        return 1
    else:
        return 2*powers_of_two(n-1)


def doubler(lst):
    '''Print out double the list items in nested lists

    >>> doubler([1, [2, [3], 4], 5])
    2 4 6 8 10

    '''

    for item in lst:
        if isinstance(item, list):
            doubler(item)
        else:
            print (2 * item),

def traversal(files):
    '''Print out the directories in a file tree

    >>> traversal({"/":{"tmp":{"bin":{}, "stuff":{}}, "src":{"florie":{}, "practice":{}}}})
    /
    tmp
    bin
    stuff
    src
    florie
    practice

    '''

    for k, v in files.iteritems():

        print k
        traversal(v)

def length(lst):
    '''Find the length of a list recusrsively

    >>> length([1,2,3,4])
    4

    >>> length([])
    0

    '''

    if lst == []:
        return 0
    else:
        return 1 + length(lst[1:])



def multiply_list(lst):
    """Multiply all the elements in a list using recursion.
    
    
    >>> multiply_list([5, 2, 1, 4, 3, 6])
    720

    >>> multiply_list([5, 24, 48, 88])
    506880

    >>> multiply_list([5, 24, 48, 88, 0])
    0
    """
    if lst == []:
        return 1
    else:
        return lst[0] * multiply_list(lst[1:])


def factorial(n):
    """Return the factorial of n.

    The factorial is the result of multiplying all integers from 1...n.

    >>> factorial(1)
    1

    >>> factorial(2)
    2

    >>> factorial(3)
    6

    >>> factorial(4)
    24
    """

    if n == 1:
        return 1
    else:
        return n * factorial(n-1)



def sum_list(lst):
    """Sum the items in the list without using loops or the sum() function.

    >>> sum_list([5, 2, 1, 4, 3, 6])
    21

    >>> sum_list([5, 24, 48, 88])
    165
    """

    if lst == []:
        return 0
    else:
        return lst[0] + sum_list(lst[1:])


def reverse(lst):
    """Reverse a list recursively, without loops, reverse() function or list[::-1].

    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]

    >>> reverse([])
    []
    """

    if lst == []:
        return []
    else:
        return reverse(lst[1:]) + [lst[0]]




def fibonacci(n):
    """Return the nth fibonacci number.

    The nth fibonacci number is defined as:

       fibonacci(n) = fibonacci(n-1) + fibonacci(n-2)

    Use recursion to solve this.

    >>> fibonacci(1)
    1

    >>> fibonacci(2)
    1

    >>> fibonacci(3)
    2

    >>> fibonacci(4)
    3

    >>> fibonacci(5) 
    5

    >>> fibonacci(6)
    8

    >>> fibonacci(7)
    13

    >>> fibonacci(8)
    21

    >>> fibonacci(9)
    34
    """

    if n == 1:
        return 1
    elif n < 1:
        return 0
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def find(lst, i):
    """Find item i in the list lst.

    If the item is in the list, return it. Otherwise, return None.

    Use recursion to solve this.

    >>> find(["a", "b", "c"], "a")
    'a'

    >>> find(["a", "b", "c"], "c")
    'c'

    >>> find(["a", "b", "c"], "d")
    """

    if lst == []:
        return None
    elif lst[0] == i:
        return i
    else:
        return find(lst[1:], i)        


def is_palindrome(some_string):
    """Is some_string a palindrome?

    A palindrome is any string that is the same forwards and backwords
    (e.g., "radar", "racecar", "aibohphobia")

    Solve this using recursion.

    >>> is_palindrome("a")
    True

    >>> is_palindrome("hello")
    False

    >>> is_palindrome("racecar")
    True

    >>> is_palindrome("foof")
    True

    >>> is_palindrome("foaf")
    False
    """

    if some_string == "":
        return True
    elif len(some_string) == 1:
        return True
    elif some_string[0] != some_string[-1]:
        return False
    else:
        return is_palindrome(some_string[1:-1])


def is_palindrome2(some_string):
    """Another palindrome solution

    Reverse the string and compare.

    >>> is_palindrome2("a")
    True

    >>> is_palindrome2("hello")
    False

    >>> is_palindrome2("racecar")
    True

    >>> is_palindrome2("foof")
    True

    >>> is_palindrome2("foaf")
    False
    """
    return reverse_string(some_string) == some_string

def reverse_string(some_string):
    if some_string == "":
        return ""
    else:
        return reverse_string(some_string[1:]) + some_string[0]



# def magic_index(lst):
#     """Does a sorted distinct list of integers have a index such that the 
#     list element's index = it's value
    
#     Solve with recursion.


#     >>> magic_index([0,1,2])
#     0 1 2

#     """

#     if len(lst) == 1 and lst[0] == 0:
#         return 0
#     else:
#         n = 1 + magic_index(lst[:-1])
#         if lst[n] == n:
#             print n,
#             return n




# def fold_paper(width, height, folds):
#     """Find the dimensions of a folded piece of paper.

#     Given a width and height of a piece of paper, and the number of times to fold it,
#     return the final dimensions (as a tuple of width, height) of the paper. Assume that
#     you always fold in half along the longest edge of the sheet (if they are the same
#     length, fold along the width first.)

#     >>> fold_paper(8.5, 11, 1)
#     (8.5, 5.5)

#     >>> fold_paper(8.5, 11, 2)
#     (4.25, 5.5)

#     >>> fold_paper(8.5, 11, 3)
#     (4.25, 2.75)

#     >>> fold_paper(8.5, 11, 4)
#     (2.125, 2.75)

#     >>> fold_paper(8.5, 11, 5)
#     (2.125, 1.375)

#     >>> fold_paper(10, 10, 2)
#     (5.0, 5.0)

#     >>> fold_paper(10, 10, 4)
#     (2.5, 2.5)

#     Let's make sure we handle the case of even sizes:

#     >>> fold_paper(10, 10, 1)
#     (5.0, 10.0)
#     """

#     pass


# def count_up(n, target):
#     """Print all integers from n to target, inclusive.
    
#     >>> count_up(1, 5)
#     1
#     2
#     3
#     4
#     5

#     >>> count_up(0, 2)
#     0
#     1
#     2

#     >>> count_up(-1, 1)
#     -1
#     0
#     1

#     >>> count_up(0, 0)
#     0

#     >>> count_up(1, 0)
#     """

#     pass


# ###########################################################################################

if __name__ == "__main__":
    import doctest
    doctest.testmod()