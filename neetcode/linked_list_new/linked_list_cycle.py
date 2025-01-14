from typing import Optional
class ListNode:
    def __init__(self, val = 0, next=None):
        self.val = val
        self.next = next

class Solution:
    def linked_list_cycle(self, head:Optional[ListNode])->bool:
        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False

    def traverse(self,head:ListNode | None):
        current = head
        while current:
            if current.next is None:
                print(str(current.val) + " -> None")
            else:
                print(str(current.val) + " -> ", end='')
            current = current.next

def main():
    solution = Solution()
    head = ListNode(1)
    head.next = ListNode(2)
    head.next.next = ListNode(3)
    head.next.next.next = ListNode(4)
    head.next.next.next = head.next
    
    list_has_cycle = solution.linked_list_cycle(head)
    print(list_has_cycle)

if __name__ == "__main__":
    main()


