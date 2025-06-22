# Definition for singly-linked list. 
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional, List

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function: Convert list to linked list
def list_to_linkedlist(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function: Convert linked list to list
def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test inputs
inputs = [
    [1, 2, 3, 4, 5],  # Example 1
    [1, 2],           # Example 2
    []                # Example 3
]

# Solution class
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        curr = head
        next = None

        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        return prev

# Test execution
sol = Solution()
for i, arr in enumerate(inputs, 1):
    head = list_to_linkedlist(arr)
    reversed_head = sol.reverseList(head)
    print(f"Example {i} Output:", linkedlist_to_list(reversed_head))
