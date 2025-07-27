# Leetcode 83: Remove Duplicates from Sorted List
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy
        current = head
        
        while current:
            if current.next and current.val == current.next.val:
                val = current.val
                while current and current.val == val:
                    current = current.next
                prev.next = current
            else:
                prev = current
                current = current.next

        return dummy.next

    
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
    s.traverseList(s.deleteDuplicates(head))
    
if __name__ == '__main__':
    main()