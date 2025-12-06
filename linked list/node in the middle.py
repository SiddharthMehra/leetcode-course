def get_middle(head):
    length = 0
    dummy = head
    while dummy:
        length+=1
        dummy=dummy.next
    
    for _ in range(length//2):
        head = head.next
    
    return head.val

# slow-fast pointer approach

def get_middle(head):
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow.val