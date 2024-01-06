'''
Call reverse linklist 
run while loop , return false if data don't match
otherwise return outside true
'''
from reverse_list import reverse_linked_list
from linked_list import LinkedList

def check_palindrome(node:LinkedList):
    reverse_node = reverse_linked_list(node)
    current1 = node.head
    current2 = reverse_node.head
    while current1 and current2:
        if current1.data != current2.data:
            return False
        current1 = current1.next
        current2 = current2.next
    return True

def main():
    linkedlist = LinkedList()
    linkedlist.add_to_tail(0)
    linkedlist.add_to_tail(1)
    linkedlist.add_to_tail(2)
    linkedlist.add_to_tail(1)
    linkedlist.add_to_tail(0)
    linkedlist.traverse()
    print(check_palindrome(linkedlist))

    linkedlist = LinkedList()
    linkedlist.add_to_tail(0)
    linkedlist.add_to_tail(1)
    linkedlist.add_to_tail(1)
    linkedlist.add_to_tail(0)
    linkedlist.traverse()
    print(check_palindrome(linkedlist))

    linkedlist = LinkedList()
    linkedlist.add_to_tail(0)
    linkedlist.add_to_tail(2)
    linkedlist.add_to_tail(1)
    linkedlist.add_to_tail(0)
    linkedlist.traverse()
    print(check_palindrome(linkedlist))



if __name__ == "__main__":
    main()
