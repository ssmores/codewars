"""Fundamental Problems from CodeWars.

Linked Lists - Get Nth

Implement a GetNth() function that takes a linked list and an integer index and returns the node stored at the Nth index position. GetNth() uses the C numbering convention that the first node is index 0, the second is index 1, ... and so on. So for the list 42 -> 13 -> 666, GetNth() with index 1 should return Node(13);

getNth(1 -> 2 -> 3 -> null, 0).data === 1
getNth(1 -> 2 -> 3 -> null, 1).data === 2
The index should be in the range [0..length-1]. If it is not, GetNth() should throw/raise an exception (InvalidArgumentException in PHP). You should also raise an exception (InvalidArgumentException in PHP) if the list is empty/null/None.


Example Tests:

test.it("tests for getting the Nth node in a linked list.")
list = build_one_two_three()
test.assert_equals(get_nth(list, 0).data, 1, "First node should be located at index 0.")
test.assert_equals(get_nth(list, 1).data, 2, "Second node should be located at index 1.")
test.assert_equals(get_nth(list, 2).data, 3, "Third node should be located at index 2.")
test.expect_error("Invalid index value should throw error.", lambda : get_nth(list, 3))
test.expect_error("Invalid index value should throw error.", lambda : get_nth(list, -1))
test.expect_error("Invalid index value should throw error.", lambda : get_nth(list, 100))
test.expect_error("None linked list should throw error.", lambda : get_nth(None, 0))
"""

# My solution:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    """Given a linked list, find the Nth node at specified index value."""
    
    count = 0
    is_found = False
    current = node
    while current:
        if count == index:
            is_found = True
            return current
        else:
            count += 1
            current = current.next
    if not is_found:
        try:
            current.next
        except:
            raise IndexError    


# Alternative answer
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    v = -1
    n = node
    while n:
        v += 1
        if v == index:
          return n
        n = n.next
    
    raise ValueError


# Alternative answer
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def get_nth(node, index):
    # Your code goes here.
    if node is None or index < 0 :
        raise LookupError('invalid index')
    for i in range(index):
        if node.next is None:
            raise IndexError('index out of range')
        node = node.next
    return node
