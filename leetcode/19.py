from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        s = self.sizeOfList(head)
        targetNode = s - n + 1
        
        if targetNode == 1:
            return head.next
        
        temp = head
        prev = None
        
        for _ in range(1, targetNode):
            prev = temp
            temp = temp.next
            if not temp:
                return head
        
        if temp:
            prev.next = temp.next
            
        return head
    
    def sizeOfList(self, head: ListNode):
        count = 0
        while head:
            count += 1
            head = head.next
        return count
    
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
    head = s.append(head, 4)
    head = s.append(head, 5)
    
    s.traverseList(head)
    s.traverseList(s.removeNthFromEnd(head, 2))
    
if __name__ == '__main__':
    main()