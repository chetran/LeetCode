import math
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Given the head of a singly linked list, return the middle node of the linked list.
#If there are two middle nodes, return the second middle node.

def middleNode(head : ListNode):
    def loopThrough(head, currrentLength):
            if head.next == None:
                stop = math.floor(currrentLength / 2)
                if currrentLength % 2 == 0:
                    stop -= 1
                return stop, head
            stop, node = loopThrough(head.next, currrentLength + 1)
            if stop == 0:
                return stop, node
            else:
                return stop - 1, head
                
    return loopThrough(head, 1)[1]

b = ListNode(3, ListNode(4, ListNode(5, None)))
a = ListNode(1, ListNode(2, b))

print(middleNode(a) == b)
