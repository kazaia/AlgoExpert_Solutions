# Reserve linked list

#Time complexity: O(n)
#Space complexity: O(1)


def reverseLinkedList(head):
    p1 = None
    p2 = head
    while p2:
        p3 = p2.next
        p2.next = p1
        p1 = p2
        p2 = p3
    return p1    

