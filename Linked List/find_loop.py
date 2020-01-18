# Find loop 
# O(n) time / O(1) space 

# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def findLoop(head):
    fast = slow = head
	fast = fast.next.next
	slow = slow.next
	while fast != slow:
		fast = fast.next.next
		slow = slow.next
	fast = head
	while fast != slow: 
		fast = fast.next
		slow = slow.next
	return fast	
	




	
