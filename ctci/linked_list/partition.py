from linked_list import LinkedList

def create_partition(node: LinkedList, x: int) -> LinkedList:
    current = node.head
    head = current
    tail = current
    while(current):
        next_node = current.next
        if current.data < x:
            current.next = head #type:ignore
            head = current
        else:
            tail.next = current #type:ignore
            tail = current

        current = next_node
    tail.next = None #type:ignore
    linkedList = LinkedList()
    linkedList.head = head
    return linkedList

def main():
    node = LinkedList()
    node.add_to_tail(3)
    node.add_to_tail(5)
    node.add_to_tail(8)
    node.add_to_tail(5)
    node.add_to_tail(10)
    node.add_to_tail(2)
    node.add_to_tail(1)
    node.traverse()
    new_node = create_partition(node, 5)
    new_node.traverse()


if __name__ == '__main__':
    main()
