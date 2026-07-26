# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        tail = dummy
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next = list1 ## tạo ra mũi tên từ dummy => node 
                list1= list1.next ## setup mũi tên cho node 
            else:
                tail.next= list2
                list2 = list2.next
            tail= tail.next ## Dịch tail sang node hiên tại
        ## Lúc này 1 trong 2 list sẽ hết ptu trc thì ta chỉ việc nối node còn phần tử vào list output
        ## Và bởi linked lists đã được sorted rồi nên khi nối phần đuôi của output với linkedlist còn phần tử thì tất cả những cái sau đó vx follow
        ## Ex input: 1,2,4,5,6
                  ##    1,3 
                  ##  => 1 ,2,3 hết list 2 => nối mỗi đuôi 3 vào phần còn lại của list 1 
               ##   => tail.next = list1
        if list1:
            tail.next= list1
        else:
            tail.next= list2
        return dummy.next


                
        