from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s = self.getSum(l1) + self.getSum(l2)
        return self.intToList(s)
    
    def getSum(self, head: Optional[ListNode]) -> int:
        s = 0
        count = 0
        while head:
            s += head.val * pow(10, count)
            count += 1
            head = head.next
        return s
    
    def intToList(self, number: int) -> Optional[ListNode]:
        if number == 0:
            return ListNode(0)
        
        dummy = ListNode(0)
        head = dummy
        while number > 0:
            head.next = ListNode(number % 10)
            head = head.next
            number //= 10
        return dummy.next

    
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
    list1 = s.append(None, 2)
    list1 = s.append(list1, 4)
    list1 = s.append(list1, 3)
    
    list2 = s.append(None, 5)
    list2 = s.append(list2, 6)
    list2 = s.append(list2, 4)
    
    result = s.addTwoNumbers(list1, list2)
    s.traverseList(result)

if __name__ == '__main__':
    main()
