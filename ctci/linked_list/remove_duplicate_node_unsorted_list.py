from linked_list import LinkedList, Node

def remove_duplicate(linkedlist: LinkedList):
    current = linkedlist.head
    unique = set()
    previous = None
    while(current):
        if current.data not in unique:
            unique.add(current.data)
        else:
            previous.next = current.next #type:ignore
            current.next = None
        previous = current
        current = current.next


def main():
    linkedlist = LinkedList()
    linkedlist.add_to_tail(4)
    linkedlist.add_to_tail(2)
    linkedlist.add_to_tail(3)
    linkedlist.add_to_tail(2)
    linkedlist.traverse()
    remove_duplicate(linkedlist)
    linkedlist.traverse()


if __name__ == "__main__":
    main()


