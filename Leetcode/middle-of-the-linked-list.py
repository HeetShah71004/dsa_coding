# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional, List

# Actual ListNode class
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to convert list to linked list
def list_to_linkedlist(values: List[int]) -> Optional[ListNode]:
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper function to convert linked list to list
def linkedlist_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Main solution class
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

# Instantiate the solution class
sol = Solution()

# Example 1
input1 = [1, 2, 3, 4, 5]
head1 = list_to_linkedlist(input1)
middle1 = sol.middleNode(head1)
print("Example 1 Output:", linkedlist_to_list(middle1))  # Output: [3, 4, 5]

# Example 2
input2 = [1, 2, 3, 4, 5, 6]
head2 = list_to_linkedlist(input2)
middle2 = sol.middleNode(head2)
print("Example 2 Output:", linkedlist_to_list(middle2))  # Output: [4, 5, 6]
