# 第四周学习笔记
##  102.二叉树的层序遍历
> 题目描述：层序遍历就是逐层地，从左到右访问所有结点，也就是BFS的走法。因此使用BFS的解题思路。
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        levels=[]
        #terminator
        if not root:
            return levels
        def helper(node,level):
            #start with current level
            if len(levels)==level:
                levels.append([])
            
            #append the current node value
            levels[level].append(node.val)

            #process child nodes for the next level
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
        helper(root,0)
        return levels
```
