# Leetcode 876. Middle of the Linked List
# Given the head of a singly linked list, return the middle node of the linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
	def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
		ahead = head
		
		while ahead and ahead.next:
			ahead = ahead.next.next
			head = head.next
		
		return head