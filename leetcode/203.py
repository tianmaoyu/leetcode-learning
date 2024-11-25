

class ListNode:
    def __init__(self,val=None,next_node:'ListNode'=None):
        self.val:int=val
        self.next_node:ListNode=next_node


def remove(head:ListNode, val):
    # if not head: return head
    # head.next= self.removeElements(head.next,val)

    # if head.val==val:
    #     return head.next

    # return head

    while head and head.val == val:
        head = head.next

    if head is None:
        return head

    pred = head
    while pred.next:
        if pred.next and pred.next.val == val:
            del_node = pred.next
            pred.next = del_node.next
            del_node.next = None
        else:
            pred = pred.next
    return head