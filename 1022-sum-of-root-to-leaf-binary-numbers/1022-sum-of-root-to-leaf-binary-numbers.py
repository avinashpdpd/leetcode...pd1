# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root,path):
            if root is None:
                return 0
            path+=str(root.val)
            if root.left is None and root.right is None:
                print(path)
                return int(path,2)
            return dfs(root.left,path)+dfs(root.right,path)
        return dfs(root,'')
        
        '''
        def dfs(root, path):
            if root is None: return 0
            path += str(root.val)
            
            if root.left is None and root.right is None:
                print(path)
                return int(path, 2)
            
            return dfs(root.left, path) + dfs(root.right, path)
        
        return dfs(root, '')'''
            
        
        