from re import S
from typing import Optional
class ListNode:
    def __init__(self,val = 0, next= None) -> None:
        self.val = val
        self.next = next

class Solution:
    def remove_nth_node_from_end_of_list(self, head:Optional[ListNode],n:int)->Optional[ListNode]:
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1

        while right:
            left = left.next
            right = right.next

        left.next = left.next.next
        return dummy.next

def main():
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    n = 2
    result_node = solution.remove_nth_node_from_end_of_list(head, n)
    print(result_node)

if __name__ == "__main__":
    main()

            
