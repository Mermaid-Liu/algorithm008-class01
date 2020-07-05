class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        from collections import deque
        layer=deque()
        layer.append(root)
        res=[]
        while layer:
            cur_layer=[]
            for _ in range(len(layer)):
                node=layer.popleft()
                cur_layer.append(node.val)
                if node.left:
                    layer.append(node.left)
                if node.right:
                    layer.append(node.right)
            res.append(cur_layer)
        return res
