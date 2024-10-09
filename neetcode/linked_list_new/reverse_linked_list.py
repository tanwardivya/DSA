from typing import Any, Optional
class ListNode:
    def __init__(self, data:Any)-> None:
        self.data = data
        self.next: ListNode | None = None

class Solution:
    def reverse_linked_list(self, head:ListNode)-> Optional[ListNode]:
        previous : ListNode | None = None
        current = head

        while current:
            temp = current.next
            current.next = previous
            previous = current
            current = temp

        return previous
    
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
    reversed_head = solution.reverse_linked_list(head)
    solution.traverse(reversed_head)

if __name__ == "__main__":
    main()





