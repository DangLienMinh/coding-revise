from LinkedList import LinkedList

def loop_detection(li):
    fast = li.head 
    slow = li.head
    while fast and fast.next:
        fast = fast.next.next
        slow = slow.next
        if fast == slow:
            break
    if fast is None or fast.next is None:
        return None 
    slow = li.head
    while slow != fast:
        slow = slow.next
        fast = fast.next 
    return fast

def print_last_linkedlist(li,l2):
    if li is None:
        return None 
    print_last_linkedlist(li.next,l2)
    l2.add(li.value)
    

l1 = LinkedList()
l1.generate(5,0,9)
l2 = LinkedList()
print_last_linkedlist(l1.head,l2)
print l1
print "NEXT"
print l2 
    