class Node():
    def __init__(self, x):
        self.data = x
        self.next = None

def bubble_sort(head):
    if not head or not head.next:
        return head
    
    dummy = Node(0)
    dummy.next = head
    
    swapped = True
    while swapped:
        swapped = False
        prev = dummy
        current = dummy.next
        while current and current.next:
            if current.data > current.next.data:
                # change nodes
                node = current.next 
                current.next = node.next
                node.next = current
                prev.next = node
                
                swapped = True
                prev = node
            else:
                prev = current
                current = current.next
    return dummy.next
                
    

def print_list(head):
    while head:
        print(head.data, end=" ")
        head = head.next
    print()
        
if __name__ == "__main__":
  
  	# Create a hard-coded linked list:
	# 5 -> 1 -> 32 -> 10 -> 78
    head = Node(5)
    head.next = Node(1)
    head.next.next = Node(32)
    head.next.next.next = Node(10)
    head.next.next.next.next = Node(78)

    head = bubble_sort(head)
    print_list(head)