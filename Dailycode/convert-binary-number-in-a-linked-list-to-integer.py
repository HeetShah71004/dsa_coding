# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        ans, curr = 0, head
        while curr:
            ans = (ans << 1) + curr.val
            curr = curr.next
        return ans

# Helper function to create linked list from a list
def create_linked_list(arr):
    dummy = ListNode()
    curr = dummy
    for num in arr:
        curr.next = ListNode(num)
        curr = curr.next
    return dummy.next

# Example 1:
head1 = create_linked_list([1, 0, 1])
sol = Solution()
print("Example 1 Output:", sol.getDecimalValue(head1))  # Output: 5

# Example 2:
head2 = create_linked_list([0])
print("Example 2 Output:", sol.getDecimalValue(head2))  # Output: 0
