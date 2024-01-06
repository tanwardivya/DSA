from linked_list import LinkedList

def find_intersection_of_two_linked_list(ll1:LinkedList, ll2:LinkedList):
    size1 = ll1.size()
    size2 = ll2.size()
    tail1 = find_tail_of_linked_list(ll1)
    tail2 = find_tail_of_linked_list(ll2)
    if tail1 != tail2:
        return
    longer = ll2 if size1 < size2 else ll1
    shorter = ll1 if size1 < size2 else ll2
    skipped_node = find_kth_node(longer, abs(size1 - size2))
    print(f'Skipped Node:{skipped_node.data}')
    shorter_current = shorter.head
    while shorter_current != skipped_node:
        shorter_current = shorter_current.next
        skipped_node = skipped_node.next

    return shorter_current

def find_tail_of_linked_list(ll:LinkedList):
    current = ll.head
    while current.next:
        current = current.next
    return current


def find_kth_node(ll:LinkedList, k:int):
    current = ll.head
    while k > 0 and current:
        current = current.next
        k-=1
    return current
    


def main():
    ll1 = LinkedList()
    ll1.add_to_tail(3)
    ll1.add_to_tail(1)
    ll1.add_to_tail(5)
    ll1.add_to_tail(9)
    ll1.add_to_tail(7)
    tail = find_tail_of_linked_list(ll1)
    ll1.add_to_tail(2)
    ll1.add_to_tail(1)
    ll1.traverse()
    ll2 = LinkedList()
    ll2.add_to_tail(4)
    ll2.add_to_tail(6)
    tail2 = find_tail_of_linked_list(ll2)
    tail2.next = tail
    ll2.traverse()
    result = find_intersection_of_two_linked_list(ll1,ll2)
    print(f'Node:{result.data}')

    
if __name__ == "__main__":
    main()



