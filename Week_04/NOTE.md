# 第四周学习笔记
##  102.二叉树的层序遍历
> 解法1:BFS（广度优先搜索方法，逐层迭代）
```
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        result=[]
        queue=[root]
        while queue:
                node=[]
                child=[]
                for item in queue:
                    child.append(item.val)
                    if item.left:
                        node.append(item.left)
                    if item.right:
                        node.append(item.right)
                result.append(child)
                queue=node
        return result
```
> 解法2:DFS（深度优先搜索方法，用一个level来记录当前进行到了哪一层）
```
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result=[]
        if not root:
            return []
        def helper(node,level):
            if len(result)==level:
                result.append([])
            result[level].append(node.val)
            if node.left:
                helper(node.left,level+1)
            if node.right:
                helper(node.right,level+1)
        helper(root,0)
        return result
```

