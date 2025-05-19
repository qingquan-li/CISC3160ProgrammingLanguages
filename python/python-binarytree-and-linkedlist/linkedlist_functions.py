"""
Write each of the following pure functions on LinkedList.

1. Test if a list is sorted in ascending order.
2. Merge two sorted lists.
3. Test if a list is cyclic.
4. Remove duplicates from a sorted list.
5. Test if a list is palindromic.
"""

class ListNode:
    """A node in a singly linked list."""
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

# Helper functions (not part of the core requirements):
def build_list(arr):
    """Builds a linked list from a Python list and returns its head."""
    head = None
    for x in reversed(arr):
        head = ListNode(x, head)
    return head

def to_list(head):
    """Converts a linked list back into a Python list of values."""
    out = []
    node = head
    while node:
        out.append(node.val)
        node = node.next
    return out


# 1. Test if a list is sorted in ascending order.
def is_sorted(head):
    while head and head.next:
        if head.val > head.next.val:
            return False
        head = head.next
    return True


# 2. Merge two sorted lists.
def merge(list1, list2):
    # Edge cases
        if not list1:
            return list2
        if not list2:
            return list1

        temp = ListNode(0)
        current = temp

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        # If list1 still has nodes
        if list1:
            current.next = list1
        # If list2 still has nodes
        if list2:
            current.next = list2

        return temp.next


# 3. Test if a list is cyclic.
def is_cyclic(head):
    if not head or not head.next:
            return False
    # two pointers
    slow = head
    fast = head
    while fast.next:
        if not fast.next.next:
            return False
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True
    return False


# 4. Remove duplicates from a sorted list.
def remove_duplicates(head):
    current = head
    while current:
        while current.next and current.val == current.next.val:
            current.next = current.next.next
        current = current.next
    return head


# 5. Test if a list is palindromic.
def is_palindromic(head):
    """
    Returns True if the linked list reads the same forwards and backwards.
    Converts to a Python list of values, then does a two-pointer check.
    """
    lst = []
    while head:
        lst.append(head.val)
        head = head.next
    
    first, last = 0, len(lst) - 1
    while first < last:
        if lst[first] != lst[last]:
            return False
        first += 1
        last -= 1
    return True


# Example usage

print("1. Test if a list is sorted in ascending order.")
a = build_list([1, 2, 2, 3])
print(is_sorted(a))  # True

print("\n2. Merge two sorted lists.")
b = build_list([2, 3, 4])
print(to_list(merge(a, b)))  # [1, 2, 2, 2, 3, 3, 4]

print("\n3. Test if a list is cyclic.")
c = build_list([1, 2, 3])
c.next.next.next = c.next  # make a small cycle
print(is_cyclic(c))  # True
print(is_cyclic(a))  # False

print("\n4. Remove duplicates from a sorted list.")
d = build_list([1, 1, 2, 3, 3])
print(to_list(remove_duplicates(d)))  # [1,2,3]

print("\n5. Test if a list is palindromic.")
e = build_list([1, 2, 3, 2, 1])
print(is_palindromic(e))  # True
print(is_palindromic(a))  # False
