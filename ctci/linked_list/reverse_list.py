from linked_list import LinkedList
from node import Node

def reverse_linked_list(node:LinkedList):
    previous = None 
    current = node.head

    while current is not None:
        new_node = Node(current.data)
        new_node.next = previous
        previous = new_node
        current = current.next

    linked_list = LinkedList()
    linked_list.head = previous
    return linked_list


def main():
    node1 = LinkedList()
    node1.add_to_tail(1)
    node1.add_to_tail(2)
    node1.add_to_tail(3)
    node1.add_to_tail(4)
    node1.add_to_tail(5)
    node1.traverse()
    result = reverse_linked_list(node1)
    result.traverse()

if __name__ == "__main__":
    main()
    



