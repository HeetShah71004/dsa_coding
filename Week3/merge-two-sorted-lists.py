class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        dummyNode = ListNode(-1)
        temp = dummyNode

        curr1, curr2 = list1, list2

        while curr1 and curr2:
            if curr1.val < curr2.val:
                temp.next = curr1
                curr1 = curr1.next
            else:
                temp.next = curr2
                curr2 = curr2.next
            temp = temp.next

        # Attach the remaining nodes
        temp.next = curr1 if curr1 else curr2

        return dummyNode.next

# Function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Function to print a linked list
def print_linked_list(head):
    values = []
    while head:
        values.append(str(head.val))
        head = head.next
    print(" -> ".join(values))

# Test case
list1 = create_linked_list([1, 3, 5])
list2 = create_linked_list([2, 4, 6])

solution = Solution()
merged_head = solution.mergeTwoLists(list1, list2)

print("Merged Linked List:")
print_linked_list(merged_head)
