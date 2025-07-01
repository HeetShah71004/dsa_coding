# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        l = []
        current = head
        while current:
            l.append(current.val)
            current = current.next
        return l == l[::-1]

# Helper function to convert a list to a linked list
def list_to_linkedlist(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Example 1
head1 = list_to_linkedlist([1, 2, 2, 1])
print("Example 1 Output:", Solution().isPalindrome(head1))  # Output: True

# Example 2
head2 = list_to_linkedlist([1, 2])
print("Example 2 Output:", Solution().isPalindrome(head2))  # Output: False
