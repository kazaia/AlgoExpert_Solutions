# Remove the Nth Node From End of a linked list 


# Time comlexity: O(n)
# Space complexity: O(1)

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def removeNthFromEnd(head, k):
    counter = 1
    first = head
    second = head
    while counter <= k:
        second = second.next
        counter += 1
    if second is None:
        head.value = head.next.value
        head.next = head.next.next
        return 
    while second.next is not None: 
        second = second.next 
        first = first.next
    first.next = first.next.next
    return head
        
        
