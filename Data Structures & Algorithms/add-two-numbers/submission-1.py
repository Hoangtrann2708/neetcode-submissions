# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()      # node giả
        cur = dummy             # con trỏ chạy, bắt đầu ở dummy
        carry = 0

        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0     # list nào hết thì coi như digit 0
            v2 = l2.val if l2 else 0

            total = v1 + v2 + carry
            carry = total // 10          # phần nhớ
            digit = total % 10           # chữ số viết ra

            cur.next = ListNode(digit)   # nối dây sang node mới
            cur = cur.next               # dịch con trỏ

            l1 = l1.next if l1 else None  # đi tiếp trên mỗi list (nếu còn)
            l2 = l2.next if l2 else None

        return dummy.next    # bỏ node giả, trả list thật