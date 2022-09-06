# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        """if root is None: # check if node is null
            return False
        if root.left is None and root.right is None: # check if node is a leaf
            return root.val == targetSum
        targetSum -= root.val # decrease total sum
        return (self.hasPathSum(root.left, targetSum) or self.hasPathSum(root.right, targetSum))"""
        if root is None:
            return False
        
        if root.left is None and root.right is None:
            if root.val==targetSum:
                return True
            
            
        targetSum-=root.val
        
        return (self.hasPathSum(root.left,targetSum)) or(self.hasPathSum(root.right,targetSum))
                
        
            
            