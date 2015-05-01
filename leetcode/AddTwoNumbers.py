#!/usr/bin/env python
# coding=utf-8


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # @param {ListNode} l1
    # @param {ListNode} l2
    # @return {ListNode}
    def addTwoNumbers(self, l1, l2):
        rl1 = self.reverse(l1)

    def reverse(self, l1):
        while l1 is not None:
            new_node = ListNode(l1.val)
            new_node.next = l1

            l1 = l1.next


def main():
    l1 = ListNode(1)
    l2 = ListNode(8)
    
    l1.next = l2
    
    l4 = ListNode(2)
    l5 = ListNode(4)
    l6 = ListNode(6)
    
    l4.next = l5
    l5.next = l6

    sol = Solution()
    res = sol.addTwoNumbers(l1, l4)

    while res is not None:
        print res.val
        res = res.next

if __name__ == "__main__":
    main()



