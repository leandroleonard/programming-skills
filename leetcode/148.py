# Definition for singly-linked list.
from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass
    
    def getTail(self, head):
        while head and head.next:
            head = head.next
        return head
    
    def partition(self, start, end):
        if start == end or not start or not end:
            return start, end, end
        
        pivot = end
        curr = start
        tail = pivot
        
        new_head = None
        prev_small = None
        
        while curr != pivot:
            next_node = curr.next
            if curr.val <= pivot.val:
                if not new_head:
                    new_head = curr
                    prev_small = curr
                else:
                    prev_small.next = curr
                    prev_small = curr
            else:
                tail.next = pivot
                tail = curr
            curr = next_node
        
        if prev_small:
            prev_small.next = pivot
        pivot.next = None
        tail.next = None
        
        if not new_head:
            new_head = pivot
            
        return new_head, pivot, tail
    
    def quicksort(start, end)