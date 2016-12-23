"""Fundamental Problems from CodeWars.

Linked Lists - Push & BuildOneTwoThree

Write push() and buildOneTwoThree() functions to easily update and initialize linked lists. Try to use the push() function within your buildOneTwoThree() function.

Here's an example of push() usage:

var chained = null
chained = push(chained, 3)
chained = push(chained, 2)
chained = push(chained, 1)
push(chained, 8) === 8 -> 1 -> 2 -> 3 -> null
The push function accepts head and data parameters, where head is either a node object or null/None/nil. Your push implementation should be able to create a new linked list/node when head is null/None/nil.

The buildOneTwoThree function should create and return a linked list with three nodes: 1 -> 2 -> 3 -> null

Example Tests:
test.describe("tests for inserting a node before another node.")
test.assert_equals(push(None, 1).data, 1, "Should be able to create a new linked list with push().")
test.assert_equals(push(None, 1).next, None, "Should be able to create a new linked list with push().")
test.assert_equals(push(Node(1), 2).data, 2, "Should be able to prepend a node to an existing node.")
test.assert_equals(push(Node(1), 2).next.data, 1, "Should be able to prepend a node to an existing node.")

test.describe("tests for building a linked list.")
test.assert_equals(build_one_two_three().data, 1, "First node should should have 1 as data.")
test.assert_equals(build_one_two_three().next.data, 2, "First node should should have 1 as data.")
test.assert_equals(build_one_two_three().next.next.data, 3, "Second node should should have 2 as data.")
test.assert_equals(build_one_two_three().next.next.next, None, "Third node should should have 3 as data.")
"""

# My solution:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    
def push(head, data):
    """Inserts a new head node for a linked list given a head. If head is none, creates a new linked list."""
    # Your code goes here.
    if not head:
        head = Node(data)
        return head
    else:
        current = head
        insert_node = Node(data)
        insert_node.next = current
        head = insert_node
        return head

  
def build_one_two_three():
    """Creates Nodes 1, 2, and 3 for a new linked list, using the push function."""
    # Your code goes here.
    head = push(None, 1)
    head = push(head, 2)
    head = push(head, 3)
    return head


# Alternative answer
class Node(object):
  def __init__(self, data):
    self.data = data
    self.next = None
    
def push(head, data):
  n = Node(data)
  n.next = head
  return n
  
def build_one_two_three():
  return push(push(Node(3), 2), 1)