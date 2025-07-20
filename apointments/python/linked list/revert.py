# Leetcode 206. Reverse Linked List
# Given the head of a singly linked list, reverse the list, and return the reversed list.
from typing import Optional, ListNode

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # primeiro passo criar um node vazio
        new_list = None
        
        # criar um loop que vai existir enquanto head apontar para algo
        while head:
            next_node = head.next
            head.next = new_list # apontar para o node anterior (reverter seta)
            # caminhar a lista para frente
            new_list = head
            # caminhar o next para frente
            head = next_node
            
        return new_list
            
            
        
