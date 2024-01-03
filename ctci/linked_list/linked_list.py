from typing import Union


class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None
    
    def add_to_tail(self,data):
        node = Node(data)# Creating a New Instance: When you write node = Node(data), you are calling the constructor of the Node class. The constructor is a special method that is automatically called when a new instance of a class is created. In this case, it's expected that the Node class has a constructor that takes a single argument (data) and uses it to initialize the new node.
        if self.head is None:
            self.head = node
            return
        current = self.head
        while(current.next):
            current = current.next

        current.next = node #type:ignore


    def traverse(self):
        current = self.head
        while current:
            if current.next is None:
                print(str(current.data) + " -> None")
            else:
                print(str(current.data) + " -> ", end='')
            current = current.next

    def delete(self,data):
        previous = None
        current = self.head
        while current:
            if (current.data == data):
                previous.next = current.next # type:ignore
                current.next = None
                break
            else:
                previous = current
                current = current.next

    def size(self):
        count = 0
        current = self.head 
        while current:
            count += 1
            current = current.next
        return count


def main():
    linked_list = LinkedList()
    linked_list.add_to_tail(1)
    linked_list.add_to_tail(2)
    linked_list.add_to_tail(3)
    print(linked_list.size())
    linked_list.delete(2)
    print(linked_list.size())
    linked_list.traverse()
    print(linked_list.size())

if __name__ == "__main__":
    main()



