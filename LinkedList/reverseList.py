#!/usr/bin/env python3

from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        prev = None
        while res:
            res.next, prev, res = prev, res, res.next
        return prev

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
    print(arr)
    return arr

if __name__ == '__main__':
    solution = Solution()
    print(to_python_list(solution.reverseList(to_linked_list([0,1,2,3]))) == [3,2,1,0])
    print(to_python_list(solution.reverseList(to_linked_list([1]))) == [1])
    print(to_python_list(solution.reverseList(to_linked_list([]))) == [])
