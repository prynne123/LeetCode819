# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode(0)
        cur = dummy
        carry = 0
        while l1!= None or l2 != None:
            num1 = 0
            if l1 != 0:
                num1 = l1.val
                
            num2 = 0
            if l2 != 0:
                num2 = l2.val
            sum = num1 + num2 + carry
            
            carry = sum // 10
            cur.next = ListNode(sum%10)
            cur = cur.next
            
            if l1 != None：
                l1 = l1.next
            else:
                l1 = None
                
            if l2 != None：
                l2 = l2.next
            else:
                l2 = None
        
        if carry != 0:
            cur.next = ListNode(carry)
        return dummy.next