"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        oldToNew = {}
        def dfs(node):
            if node in oldToNew:           ## Nếu node có trong map 
                return oldToNew[node]       ## Return copy của nó

            copy= Node(node.val)            ## Chưa có
                ## =>Tạo copy cho node đang xét
            oldToNew[node]= copy
                ## => Nối giá trị giữa key vs value
                       ## oldToNew{key:value      
                                 ## 1: 1  }
            for nei in node.neighbors: 
                    ## ở node gốc đang nối vs neighbor nào 
                copy.neighbors.append(dfs(nei))
                    ## copy cũng phải nối với các neighbors đó 
                    ## phải nối với copy của các node đó nên dfs(nei) dùng để check xem node đó đã có copy chưa 
            return copy
        if node:
            return dfs(node)
        return None
                
