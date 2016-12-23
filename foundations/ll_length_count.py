"""Fundamental Problems from CodeWars.
Linked Lists - Length & Count

Implement Length() to count the number of nodes in a linked list.

length(null) === 0
length(1 -> 2 -> 3 -> null) === 3
Implement Count() to count the occurrences of an integer in a linked list.

count(null, 1) === 0
count(1 -> 2 -> 3 -> null, 1) === 1
count(1 -> 1 -> 1 -> 2 -> 2 -> 2 -> 2 -> 3 -> 3 -> null, 2) === 4
I've decided to bundle these two functions within the same Kata since they are both very similar.

The push() and buildOneTwoThree() functions do not need to be redefined.
"""

# My solution:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    """Provides length of linked list."""
    if not node:
        return 0
    count = 0
    current = node
    while current:
        count +=1
        current = current.next
    return count
  
def count(node, data):
    """Counts occurances of data in linked list."""
    if not node:
        return 0
    count = 0
    current = node
    while current:
        if current.data == data:
            count +=1
        current = current.next
    return count



# Alternative answer
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
def length(node):
    leng = 0
    while node:
        leng += 1
        node = node.next
    return leng
  
def count(node, data):
    c = 0
    while node:
        if node.data==data:
            c += 1
        node = node.next
    return c
