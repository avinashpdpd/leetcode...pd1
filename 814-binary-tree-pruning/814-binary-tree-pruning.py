# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
#postord-->left right root
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """ if not root: return None
        root.left, root.right = self.pruneTree(root.left), self.pruneTree(root.right)
        return root if (root.left or root.right or root.val == 1) else None"""
        
        
        
        if not root:
            return None
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
            
        if root.val==0 and not root.right and not root.left:
            return None
        else:
            return root
        
                
        