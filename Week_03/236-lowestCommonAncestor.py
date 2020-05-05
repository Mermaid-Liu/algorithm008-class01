# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        dict={root:None}
        def dfs(node):
            if node:
                if node.left:
                    dict[node.left]=node
                if node.right:
                    dict[node.right]=node
                dfs(node.left)
                dfs(node.right)
        dfs(root)
        l1,l2=p,q
        while l1!=l2:
            l1=dict.get(l1,q)
            l2=dict.get(l2,p)
        return l1
