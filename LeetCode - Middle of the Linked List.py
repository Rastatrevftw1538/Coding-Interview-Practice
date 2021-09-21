# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        listSize = 0
        listCount = 0
        headStart = head
        while head:
            listSize += 1
            head = head.next
        head = headStart
        while head:
            listCount += 1
            if listCount > listSize/2:
                if listCount/2 == 0:
                    head = head.next
                    return head
                return head
            else:
                head = head.next
        return head
        