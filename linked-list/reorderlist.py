#!/usr/bin/env python3

from ll_utils import checker, to_python_list, to_linked_list, ListNode
from typing import Optional

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        return

if __name__ == '__main__':
    solution = Solution()
    checker(to_python_list(solution.reorderList(to_linked_list([2,4,6,8]))), [2,8,4,6])
    checker(to_python_list(solution.reorderList(to_linked_list([2,4,6,8,10]))), [2,10,4,8,6])
