from linked_list import LinkedList,Node

def find_kth_last_element(linkedlist:LinkedList, k:int):
    current = linkedlist.head
    size = linkedlist.size()
    length = size - k 
    for i in range(length):
        current = current.next #type:ignore
    return current.data #type:ignore

def main():
    linkedlist = LinkedList()
    linkedlist.add_to_tail(4)
    linkedlist.add_to_tail(2)
    linkedlist.add_to_tail(3)
    linkedlist.add_to_tail(5)
    linkedlist.traverse()
    result = find_kth_last_element(linkedlist,k=3)
    print(result)
   
if __name__ == "__main__":
    main()