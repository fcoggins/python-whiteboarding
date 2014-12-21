import linkedlists

def find_last(n):
    '''You have a circle of n chairs. Remove every other chair continuously until 
    there is one chair left. What is the last remaining chair. Solution uses linked lists.

    >>> find_last(5)
    3

    >>> find_last(12)
    9

    >>> find_last(11)
    7

    '''

    cycle = linkedlists.Cycle(n)
    node = cycle.head
    prev = cycle.head
    counter = 0
    while node != node.next:
        if counter%2 != 0:
            prev.next = node.next
            prev = node.next
        node = node.next
        counter += 1
    return node.next.data + 1

if __name__ == "__main__":
    import doctest
    doctest.testmod()