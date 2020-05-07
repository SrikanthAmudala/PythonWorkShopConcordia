def middleNode(head: ListNode) -> ListNode:
    count = 0
    nextValue = head
    while nextValue!=None:
        count+=1
        nextValue = nextValue.next
    midlen = count//2
    mid = head
    for i in range(midlen):
        mid = mid.next
    return mid
    


def middleNode(head: ListNode) -> ListNode:
    """
    using two pointers, move a by one point and b by two points each time
    so b will be twice the distance from a
    if b reaches None, your a is the mid
    """
    a = b = head
    while b!=None:
        b = b.next
        if b==None:
            return a
        a = a.next
        b = b.next
        
    return a
        