#!/usr/bin/env python3

from ll_utils import to_python_list, to_linked_list, ListNode, checker
from typing import Optional

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        p1, p2 = head, head
        while p2 and p2.next:
            p1 = p1.next
            p2 = p2.next.next
            if p1 == p2:
                return True
        return False

    def hasCycle2(self, head: Optional[ListNode]) -> bool:
        seen = set()

        while head:
            if head in seen:
                return True
            seen.add(head)
            head = head.next
        return False

if __name__ == '__main__':
    solution = Solution()
    checker(solution.hasCycle(to_linked_list([1,2,3,4])), True)
    checker(solution.hasCycle(to_linked_list([1,2])), False)
