# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.ret= root.val
        def dfs(node):
            if node is None:
                return 0
            leftGrid= max(dfs(node.left),0)
            rightGrid= max(dfs(node.right),0)

            self.ret= max(self.ret, leftGrid + node.val+ rightGrid) ## Tính path cho node hiện tại làm gốc 
            return node.val + max(leftGrid, rightGrid) ## trả về cho cha thì chỉ có thể chọn 1 trong 2 nhánh trái hoặc phaỉ , chọn nhánh nào mà lớn hơn 
        
        dfs(root)
        return self.ret

            
        