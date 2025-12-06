# advance slow pointer by k places 
def find_node(head, k):
    slow, fast = head, head
    for _ in range(k):
        fast = fast.next
    
    while fast:
        slow = slow.next
        fast = fast.next
    
    return slow