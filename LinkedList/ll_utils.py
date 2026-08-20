from typing import Optional

def checker(received, answer):
    if received != answer:
        print(f'FAILED: Received: {received}, but expected: {answer}.')
        return 
    print("PASSED!")

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_linked_list(arr: list) -> Optional[ListNode]:
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def to_python_list(head: Optional[ListNode]) -> list:
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next
    return arr
