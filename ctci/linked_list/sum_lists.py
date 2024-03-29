from linked_list import LinkedList,Node
from reverse_list import reverse_linked_list

def sum_lists(node1:LinkedList, node2:LinkedList):
    current1 = node1.head
    current2 = node2.head
    head = None 
    current = head
    carry = 0
    while(current1 and current2):
        data = current1.data + current2.data + carry
        carry = data // 10
        remainder = data % 10
        if head is None:
            head = Node(remainder)
            current = head
        else:
            temp = Node(remainder)
            current.next = temp
            current = temp
        
        current1 = current1.next
        current2 = current2.next

    if current1:
        data = current1.data + carry
        temp = Node(data)
        current.next = temp
        current = temp

    if current2:
        data = current2.data + carry
        temp = Node(data)
        current.next = temp
        current = temp

    linkedlist = LinkedList()
    linkedlist.head = head
    return linkedlist

def sum_lists_v2(node1:LinkedList, node2:LinkedList):
    '''
    Reverse node1
    Reverse node2
    Call sum_list method
    Reverse the final result
    '''
    reverse_node1 = reverse_linked_list(node1)
    reverse_node2 = reverse_linked_list(node2)
    result = sum_lists(reverse_node1, reverse_node2)
    final_result = reverse_linked_list(result)
    return final_result


def main():
    #1st example

    print("Test Case 1")
    node1 = LinkedList()
    node1.add_to_tail(7)
    node1.add_to_tail(1)
    node1.add_to_tail(6)
    node1.traverse()
    
    node2 = LinkedList()
    node2.add_to_tail(5)
    node2.add_to_tail(9)
    node2.add_to_tail(2)
    node2.traverse()
    result = sum_lists(node1, node2)
    result.traverse()
    print("Test Case 2")
    #2nd example
    node1 = LinkedList()
    node1.add_to_tail(7)
    node1.add_to_tail(1)
    node1.add_to_tail(6)
    node1.traverse()

    node2 = LinkedList()
    node2.add_to_tail(9)
    node2.add_to_tail(9)
    node2.traverse()
    result = sum_lists(node1, node2)
    result.traverse()
    
    print("Test Case 3")

    #3rd Example
    node1 = LinkedList()
    node1.add_to_tail(7)
    node1.add_to_tail(6)
    node1.traverse()

    node2 = LinkedList()
    node2.add_to_tail(5)
    node2.add_to_tail(9)
    node2.add_to_tail(2)
    node2.traverse()
    result = sum_lists(node1, node2)
    result.traverse()

def main_v2():
    print("Test Case 1")
    node1 = LinkedList()
    node1.add_to_tail(6)
    node1.add_to_tail(1)
    node1.add_to_tail(7)
    node1.traverse()
    
    node2 = LinkedList()
    node2.add_to_tail(2)
    node2.add_to_tail(9)
    node2.add_to_tail(5)
    node2.traverse()
    result = sum_lists_v2(node1, node2)
    result.traverse()


if __name__ == "__main__":
    main()
    main_v2()


        
            
