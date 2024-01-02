from linked_list import LinkedList,Node

def delete_middle_node(linkedlist:LinkedList):
    current = linkedlist.head
    previous = None
    size = linkedlist.size()
    mid = size // 2
    for i in range(mid):
        previous = current
        current = current.next #type:ignore
    previous.next =current.next #type:ignore
    current.next = None #type:ignore

def main():
    linkedlist = LinkedList()
    linkedlist.add_to_tail(4)
    linkedlist.add_to_tail(2)
    linkedlist.add_to_tail(3)
    linkedlist.add_to_tail(5)
    linkedlist.add_to_tail(7)
    linkedlist.traverse()
    delete_middle_node(linkedlist)
    linkedlist.traverse()

if __name__ == "__main__":
    main()
   