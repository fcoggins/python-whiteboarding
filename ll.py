import linkedlists



def dedupll(*argv):
    ''' Input data, create a linked list, and remove duplicates
    
    Args:
        any number of items to be contained in a linked list
    Returns:
        a linked list object with no duplicates

    >>> dedupll(2,2,2).PrintList()
    2

    >>> dedupll(1,2,1,2,3,4,5,5,2).PrintList()
    1 2 3 4 5

    >>> dedupll(1,2,"cat","Cat",3.0,3,3,"cat",4,5,5,5).PrintList()
    1 2 cat Cat 3.0 4 5

    '''

    input_list = linkedlists.LinkedList()
    for arg in argv:
        input_list.AddNode(arg)
    return input_list.DeleteDuplicate()

def dedup2(*argv):
    '''Use a dictionary'''

    input_list = linkedlists.LinkedList()
    for arg in argv:
        input_list.AddNode(arg)
    node = input_list.head
    list_to_dict = {}
    while node:
        list_to_dict[node.data] = 1
        node = node.next
    new_list = linkedlists.LinkedList()
    for k, v in list_to_dict.iteritems():
        new_list.AddNode(k)

    return new_list

def create_reversed_list(num):
    '''Create a linked list in reverse order of the digits given
    
    Args:
        An integer > 0
    Returns:
        A linked list in reverse order

    >>> create_reversed_list(927).PrintList()
    7 2 9

    >>> create_reversed_list(112).PrintList()
    2 1 1
    '''

    num_str = str(num)
    ll = linkedlists.LinkedList()
    for i in range(len(num_str)-1, -1, -1):
        ll.AddNode(int(num_str[i]))
    return ll


def add_two_numbers(ll1, ll2):
    '''Each node of a linked list stores a digit in reverse order. Return a linked
    list that contains the sum of the digits. This is from Cracking the Coding Interview
    problem #2.5

    Args:
        two linked lists
    Returns:
        a linked list that contains the sum

    >>> add_two_numbers(create_reversed_list(617), create_reversed_list(295)).PrintList()
    2 1 9

    >>> add_two_numbers(create_reversed_list(989), create_reversed_list(898)).PrintList()
    7 8 8 1

    >>> add_two_numbers(create_reversed_list(192), create_reversed_list(372)).PrintList()
    4 6 5

    >>> add_two_numbers(create_reversed_list(192), create_reversed_list(372)).PrintList()
    4 6 5

    >>> add_two_numbers(create_reversed_list(1872), create_reversed_list(1673)).PrintList()
    5 4 5 3

    >>> add_two_numbers(create_reversed_list(12), create_reversed_list(354)).PrintList()
    6 6 3

    >>> add_two_numbers(create_reversed_list(12), create_reversed_list(1999)).PrintList()
    1 1 0 2

    '''

    #find the length of list
    if ll1.Length() > ll2.Length():
        max_len = ll2.Length()
        additional_digits = ll1.Length() - ll2.Length()
        max = 1
    elif ll2.Length() > ll1.Length():
        max_len = ll1.Length()
        additional_digits = ll2.Length() - ll1.Length()
        max = 2
    else:
        max_len = ll1.Length()
        additional_digits = 0

    new_list = linkedlists.LinkedList()
    carry = 0

    #cycle through the nodes
    for i in range(max_len):
        digit = int(ll1.FindValue(i)) + int(ll2.FindValue(i)) + carry
        if digit > 9 :
            carry = 1
            digit = digit - 10
        else:
            carry = 0
        new_list.AddNode(digit)
        if i == max_len - 1 and carry == 1 and additional_digits == 0:
            new_list.AddNode(1)

    #if numbers are not the same length
    if additional_digits > 0:
        for i in range(max_len, max_len + additional_digits):
            if max == 1:
                digit = int(ll1.FindValue(i)) + carry
            else:
                digit = int(ll2.FindValue(i)) + carry
            if digit > 9:
                carry = 1
                digit = digit -10
            else:
                carry = 0
            new_list.AddNode(digit)

    return new_list


if __name__ == "__main__":
    import doctest
    doctest.testmod()




