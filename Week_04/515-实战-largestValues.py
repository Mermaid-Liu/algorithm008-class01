class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:
        if not root:
            return []
        res=[]
        queue=[]
        queue.append([root,0])
        while queue:
            cur,level=queue.pop()
            if len(res)==level:
                res.append(cur.val)
            res[level]=max(res[level],cur.val)
            if cur.left:
                queue.append([cur.left,level+1])
            if cur.right:
                queue.append([cur.right,level+1])
        return res
