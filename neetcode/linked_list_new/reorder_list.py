#Definition of Singly-LL
from re import L
from typing import Optional, Any
class ListNode:
    def __init__(self, data: Any = None):
        self.data = data
        self.next = None

class Solution:
    def reorder_list(self, head:Optional[ListNode]):
        """
        Do not return anything, modify head in-place instead.
        """
        # for only single node in the LL or empty List
        if not head or not head.next or not head.next.next:
            return

        #split the list into two halves
        mid = end = head
        while end.next and end.next.next:
            mid = mid.next
            end = end.next.next
        p2 = mid.next  #second half starts here
        mid.next = None # Break the link between the two halves
        # reverse 
        prev = None
        while p2 and p2.next:
            p2next = p2.next
            p2.next = prev
            prev = p2
            p2 = p2next
        p2.next = prev 
        # merge
        p1 = head
        while p2:
            p1next = p1.next
            p2next = p2.next
            p1.next = p2
            p2.next = p1next
            p1 = p1next
            p2 = p2next
    def traverse(self,head:ListNode | None):
        current = head
        while current:
            if current.next is None:
                print(str(current.data) + " -> None")
            else:
                print(str(current.data) + " -> ", end='')
            current = current.next

def main():
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = ListNode(5)
    reordered_list = solution.reorder_list(head)
    solution.traverse(reordered_list)

if __name__ == "__main__":
    main()










