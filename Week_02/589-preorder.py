lass Solution:
    def preorder(self, root: 'Node') -> List[int]:
        #解决树的问题，递归是首选
        res=[]
        def helper(root):
            if not root:
                return
            res.append(root.val)
            for child in root.children:
                helper(child)
        helper(root)
        return res
