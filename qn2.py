class ListNode:
    def __init__(self,value=0,next=None):
        self.value=value
        self.next=next
# meow 

def add_two_no(l1,l2):
    dummy_head=ListNode(0)
    current=dummy_head
    carry=0

    while l1 is not None or l2 is not None or carry!=0:

        l1_val=l1.value if l1 is not None else 0
        l2_val=l2.value if l2 is not None else 0

        total=l1_val+l2_val+carry
        carry=total//10
        current.next=ListNode(total%10)
        current=current.next

        if l1 is not None:
            l1=l1.next
        if l2 is not None:
            l2=l2.next
    return dummy_head.next

def create_linklist(lst):
    dummy_head=ListNode(0)
    current=dummy_head
    for num in lst:
        current.next=ListNode(num)
        current=current.next
    return dummy_head.next

def linklist_to_list(llist):
    res=[]
    while llist:
        res.append(llist.value)
        llist=llist.next
    return res


l1 = create_linklist([2, 4, 3])
l2 = create_linklist([5, 6, 4])
result = add_two_no(l1, l2)
print(linklist_to_list(result))
        

