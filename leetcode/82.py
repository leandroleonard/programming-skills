# Leetcode 83: Remove Duplicates from Sorted List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        prev = head
        current = head.next

        while current:
            if current.val == prev.val:
                while current.next and current.val == current.val:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next

        return head

    
    # Dont submit
    def append(self, head: ListNode, value: int):
        new_node = ListNode(value)
        if not head:
            return new_node
        last = head
        while last.next:
            last = last.next
            
        last.next = new_node
        return head
    
    def traverseList(self, head: Optional[ListNode]):
        while head:
            print(head.val, end=" ")
            head = head.next            
        print()
        
    
def main():
    s = Solution()
    head = s.append(None, 1)
    head = s.append(head, 2)
    head = s.append(head, 3)
    head = s.append(head, 3)
    head = s.append(head, 4)
    head = s.append(head, 4)
    head = s.append(head, 5)
    
    s.traverseList(head)
    s.deleteDuplicates(head)
    s.traverseList(head)
    
if __name__ == '__main__':
    main()