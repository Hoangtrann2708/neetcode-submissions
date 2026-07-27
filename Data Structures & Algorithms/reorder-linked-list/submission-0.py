# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        ## 1: Duyệt TOÀN Bộ LinkedList để tìm middle 
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        ## Phần reverse start from slow.next do slow = mid
        second = slow.next 
        slow.next= None
        prev= None
        while second:
            nxt= second.next
            second.next = prev
            prev = second
            second= nxt
        
        ## Bắt đầu merge 
        ##first = head = 0123
        ## second = prev = 654
        first = head
        second = prev
        while second: ## second luôn là mảng ít phần tử hơn
            nxt1, nxt2= first.next, second.next ## ghi nhớ next của 0 là 1, và của 6 là 5
            first.next= second ## 0 nối 6 
            second.next = nxt1 ## 6 nối 1
            first, second = nxt1,nxt2 ## dịch biến first và second (ban đầu là 0 và 6 bây h là 1 và 5)
        



        