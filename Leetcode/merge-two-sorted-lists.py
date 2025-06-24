# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, head1: ListNode, head2: ListNode) -> ListNode:
        if head1 is None or head2 is None:
            return head2 if head1 is None else head1

        if head1.val <= head2.val:
            head1.next = self.mergeTwoLists(head1.next, head2)
            return head1
        else:
            head2.next = self.mergeTwoLists(head1, head2.next)
            return head2
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "\n")
        head = head.next

# Example usage
if __name__ == "__main__":
    l1 = build_linked_list([1, 3, 5])
    l2 = build_linked_list([2, 4, 6])
    sol = Solution()
    merged = sol.mergeTwoLists(l1, l2)
    print("Merged Linked List:")
    print_linked_list(merged)
