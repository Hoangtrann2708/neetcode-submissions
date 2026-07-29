"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        oldListCopy= {}
        cur = head
        while cur:
            copy = Node(cur.val)
            oldListCopy[cur]= copy
            cur = cur.next
        
        cur = head
        while cur:
            copy = oldListCopy[cur]
            copy.next = oldListCopy.get(cur.next)
            copy.random = oldListCopy.get(cur.random)
            cur = cur.next
        return oldListCopy.get(head)
