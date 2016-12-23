"""Fundamental Problems from CodeWars.

Linked Lists - Insert Nth

Implement an InsertNth() function (insert_nth() in PHP) which can insert a new node at any index within a list.

InsertNth() is a more general version of the Push() function that we implemented in the first kata listed below. Given a list, an index 'n' in the range 0..length, and a data element, add a new node to the list so that it has the given index. InsertNth() should return the head of the list.

You must throw/raise an exception (InvalidArgumentException in PHP) if the index is too large.

The push() and buildOneTwoThree() (build_one_two_three() in PHP) functions do not need to be redefined. The Node class is also preloaded for you in PHP.


Example Tests:
test.it("should be able to handle an empty list.")
test.assert_equals(insert_nth(None, 0, 12).data, 12, "should be able to insert a node on an empty/None list.")
test.assert_equals(insert_nth(None, 0, 12).next, None, "value at index 1 should be None.")

test.it("should be able to insert a new node at the head of a list.")
test.assert_equals(insert_nth(build_one_two_three(), 0, 23).data, 23, "should be able to insert new node at head of list.")
test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.data, 1, "value for node at index 1 should be 1.")
test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.next.data, 2, "value for node at index 2 should be 2.")
test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.next.next.data, 3, "value for node at index 3 should be 3.")
test.assert_equals(insert_nth(build_one_two_three(), 0, 23).next.next.next.next, None, "value at index 4 should be None.")

test.it("should be able to insert a new node at index 1 of a list.")
test.assert_equals(insert_nth(build_one_two_three(), 1, 23).data, 1, "value for node at index 0 should be 1.")
test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.data, 23, "value for node at index 1 should be 23")
test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.next.data, 2, "value for node at index 2 should be 2.")
test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.next.next.data, 3, "value for node at index 3 should be 3.")
test.assert_equals(insert_nth(build_one_two_three(), 1, 23).next.next.next.next, None, "value at index 4 should be None.")

test.it("should be able to insert a new node at index 2 of a list.")
test.assert_equals(insert_nth(build_one_two_three(), 2, 23).data, 1, "head should remain unchanged after inserting new node at index 2")
test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.data, 2, "value at index 1 should remain unchanged after inserting new node at index 2")
test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.next.data, 23, "value for node at index 2 should be 23.")
test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.next.next.data, 3, "value for node at index 3 should be 3.")
test.assert_equals(insert_nth(build_one_two_three(), 2, 23).next.next.next.next, None, "value at index 4 should be None.")

test.it("should be able to insert a new node at tail of a list.")
test.assert_equals(insert_nth(build_one_two_three(), 3, 23).data, 1, "head should remain unchanged after inserting new node at tail")
test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.data, 2, "value at index 1 should remain unchanged after inserting new node at tail")
test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.next.data, 3, "value for node at index 2 should be 3.")
test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.next.next.data, 23, "value for node at index 3 should be 23.")
test.assert_equals(insert_nth(build_one_two_three(), 3, 23).next.next.next.next, None, "value at index 4 should be None.")

test.it("should raise exception if index is too large.")
test.expect_error("Invalid index value should raise error.", lambda : insert_nth(build_one_two_three(), 4, 23))

"""

# My solution:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

    
def insert_nth(head, index, data):
    """Inserts new Node at nth index given a head of a linked list."""
    
    if not head and index == 0:
        head = Node(data)
        return head
    
    
    count = 0
    is_added = False
    new_node = Node(data)

    if index == 0:
        new_node.next = head
        head = new_node
        return head
    else:
        current = head 
        while current:
            if count + 1 == index:
                new_node.next = current.next.next
                current.next = new_node
                is_added = True
                return head
            else:
                count += 1
                current = current.next

    if not is_added:
        raise IndexError


# Alternative answer
class Node(object):
    def __init__(self, data, nxt = None):
        self.data = data
        self.next = nxt
    
def insert_nth(head, index, data):
    if index == 0: return Node(data, head)
    if head and index > 0:
        head.next = insert_nth(head.next, index - 1, data)
        return head
    raise ValueError


# ALternative answer
    def __iter__(self):
        current = self
        while current is not None:
            yield current
            current = current.next

def insert_nth(head, index, data):
    if not head:
        if index == 0:
            return Node(data)
        else: raise IndexError
    else:
        prev = None
        for i, node in enumerate(head):
            if index == i:
                new_node = Node(data, node)
                if prev: prev.next = new_node
                else: head = new_node
                return head
            prev = node
        if i + 1 == index:
            node.next = Node(data)
            return head
        else: raise IndexError
