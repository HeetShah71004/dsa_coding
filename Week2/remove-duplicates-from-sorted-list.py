from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{self.val} -> {self.next}" if self.next else f"{self.val}"

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None  # Handle empty list case
        
        current = head
        while current and current.next:
            if current.val == current.next.val:
                current.next = current.next.next  # Skip the duplicate node
            else:
                current = current.next  # Move forward
        
        return head

# Helper function to convert a list into a linked list
def list_to_linked_list(arr: List[int]) -> Optional[ListNode]:
    if not arr:
        return None  # Empty list case
    
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    
    return head

# Helper function to convert a linked list back to a list
def linked_list_to_list(head: Optional[ListNode]) -> List[int]:
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test cases
head = list_to_linked_list([1, 1, 2, 3, 3])  # Convert list to linked list
result_head = Solution().deleteDuplicates(head)  # Remove duplicates
result_list = linked_list_to_list(result_head)  # Convert back to list

print(result_list)  # Output: [1, 2, 3]
