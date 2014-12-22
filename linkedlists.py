
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList(object):
    def __init__(self):
        self.head = None
        self.tail = None

    def AddNode(self, data):
        new_node = Node(data)
        if self.head == None:
            self.head = new_node

        if self.tail != None:
            self.tail.next = new_node

        self.tail = new_node

    def PrintList(self):
        node = self.head
        while node:
            print node.data
            node = node.next

    def FindNode(self, data):
        '''find the first occurence of a value in a linked list'''
        node = self.head
        prev = self.head
        n=0
        while node:
            if node.data == data:
                print "Value {} found at position {}".format(data, n)
                return prev
            n += 1
            prev = node
            node = node.next

    def FindValue(self, index):
        '''find the value at an index'''
        node = self.head
        n = 0
        while node:
            if index == n:
                return node.data
            n += 1
            node = node.next
        return "Index out of range"


    def DeleteNode(self, data):
        '''delete the first node containing particular data'''
        node_prior = self.FindNode(data)
        node_prior.next = node_prior.next.next

    def DelNodePosition(self, pos):
        '''delete the node at a certain position'''
        n=0
        node = self.head
        prev = self.head
        while node:
            if n == pos:
                prev.next = node.next
                return True
            n += 1
            prev = node
            node = node.next

    def InsNodePosition(self, pos, data):
        '''insert a node at a position and move everything down'''
        n = 0
        node = self.head
        new_node = Node(data)
        while node:
            prev = node
            node = node.next
            if pos == 0:
                new_node.next = self.head
                self.head = new_node
                return
            if pos == n + 1:
                prev.next = new_node
                new_node.next = node
                return
            n += 1
        print "List Length Exceeded, Not Added"
        return

    def Length(self):
        n = 0
        node = self.head
        while node:
            n += 1
            node = node.next
        return n

    def Min(self):
        '''Find minimum value in a list'''
        min = self.head.data
        node = self.head.next
        while node:
            if min > node.data:
                min = node.data
            node = node.next
        return min

    def Max(self):
        '''Find maximum value in a list'''
        max = self.head.data
        node = self.head.next
        while node:
            if max < node.data:
                max = node.data
            node = node.next
        return max

class Cycle(LinkedList):
    def __init__(self, num):
        LinkedList.__init__(self)
        self.numnodes = num
        for i in range(self.numnodes):
            self.AddNode(i)
        self.tail.next = self.head

    def Length(self):
        node = self.head
        n = 1
        while node != self.tail:
            n += 1
            node = node.next
        return n
