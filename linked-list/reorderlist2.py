#!/usr/bin/env python3

from ll_utils import checker, to_python_list, to_linked_list, ListNode
from typing import Optional
from math import ceil

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        order = []
        while head:
            order.append(head)
            head = head.next
        curr = order[0]
        for i in range(1, len(order)):
            if i % 2:
                n = order[-i // 2]
            else:
                n = order[i // 2]
            if curr:
                curr.next = n
                curr = curr.next
        curr.next = None

if __name__ == '__main__':
    solution = Solution()
    # checker(to_python_list(solution.reorderList(to_linked_list([2,4,6,8]))), [2,8,4,6])
    checker(to_python_list(solution.reorderList(to_linked_list([2,4,6,8,10]))), [2,10,4,8,6])
