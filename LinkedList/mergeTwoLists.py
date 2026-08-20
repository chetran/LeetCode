#!/usr/bin/env python3

from ll_utils import to_python_list, to_linked_list, ListNode, checker
from typing import Optional

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(-1)
        prev = head
        while list1 and list2:
            if list1.val <= list2.val:
                prev.next = list1
                list1 = list1.next
            else:
                prev.next = list2
                list2 = list2.next
            prev = prev.next
        
        prev.next = list1 if list1 else list2
        return head.next


if __name__ == '__main__':
    solution = Solution()
    checker(to_python_list(solution.mergeTwoLists(to_linked_list([1,2,4]), to_linked_list([1,3,5]))), [1,1,2,3,4,5]) 
    checker(to_python_list(solution.mergeTwoLists(to_linked_list([]), to_linked_list([1,2]))), [1,2]) 
    checker(to_python_list(solution.mergeTwoLists(to_linked_list([]), to_linked_list([]))), []) 

