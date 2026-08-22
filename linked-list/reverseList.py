#!/usr/bin/env python3

from ll_utils import checker, to_python_list, to_linked_list, ListNode
from typing import Optional

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        prev = None
        while res:
            res.next, prev, res = prev, res, res.next
        return prev

if __name__ == '__main__':
    solution = Solution()
    checker(to_python_list(solution.reverseList(to_linked_list([0,1,2,3]))), [3,2,1,0])
    checker(to_python_list(solution.reverseList(to_linked_list([1]))), [1])
    checker(to_python_list(solution.reverseList(to_linked_list([]))), [])
