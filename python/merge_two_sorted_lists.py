"""Merge two sorted linked lists and return it as a new list. 
   The new list should be made by splicing together the nodes of the first two lists."""

   # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        l3 = cur_node = ListNode(0)
        # Loop through nodes until one is equal to None/list is at end
        # Set reference to next value to node with lowest value
        while l1 and l2:
            if l1.val < l2.val:
                cur_node.next = l1
                l1 = l1.next
            else:
                cur_node.next = l2
                l2 = l2.next
            cur_node = cur_node.next
        # Set next to remainder of either list if it exists,
        # otherwise None
        cur_node.next = l1 or l2
        return l3.next
