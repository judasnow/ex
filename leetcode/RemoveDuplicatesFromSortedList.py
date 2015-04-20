#!/usr/bin/env python
# encoding=utf-8

# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None


class Solution:
    # @param head, a ListNode
    # @return a ListNode
    def deleteDuplicates(self, head):

        cursor = head
        current_val = None

        while cursor != None:
            current_val = cursor.val

            while cursor.next and cursor.next.val == current_val:
                cursor.next = cursor.next.next

            cursor = cursor.next
            
        return head


def main():
    l1 = ListNode(1)
    l2 = ListNode(1)
    l3 = ListNode(1)
    l4 = ListNode(4)
    l5 = ListNode(5)
    
    head = ListNode(None)
    head.next = l1
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    
    sol = Solution()
    cursor = sol.deleteDuplicates(l1)

    while cursor != None:
        print cursor.val
        cursor = cursor.next


if __name__ == "__main__":
    main()

    
