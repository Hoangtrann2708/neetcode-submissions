# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast= head
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
            if slow == fast:
                return True
        return False
            
            
            
            
            
## ta cần fast để check chưa xem đã None chưa , bởi vì nếu nó None rồi thì khi gọi fast.None sẽ bị lỗi
        
## fast với TH khi list là odd elemnts
 ##1 2 3 4 5 => fast: 1->3->5 => Bây giờ vào đk: while fast = 5 nma fast.next = None =>True and False 
  ##TA PHẢI DỪNG VÒNG LẶP NGAY nhờ 2 ĐIỀU KIỆN NÀY. NẾU KO KHI VÀO TRONG fast sẽ = fast.next.next => NOne thì k có .next => Sai

 ## fast với TH khi list là even elemnts
 ## 1 2 3 4 => fast: 1->3->None  => Bây giờ vào đk: while fast = None  KO QUAN TÂM ĐẾN ( fast.next nữa vì cái đầu đã false rồi) 
 ## ĐÂY LÀ CASE KHI KO CÓ CYCLE

 