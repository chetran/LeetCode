#!/usr/bin/env python3

from ll_utils import to_python_list, to_linked_list, ListNode, checker
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        return False

if __name__ == '__main__':
    solution = Solution()
    checker(solution.hasCycle(to_linked_list([1,2,3,4])), True)
    checker(solution.hasCycle(to_linked_list([1,2])), False)
