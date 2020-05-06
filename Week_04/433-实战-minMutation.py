class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank=set(bank)
        if end not in bank:
            return -1
        q=[(start,0)]
        dict={"A":"CGT","C":"AGT","G":"ACT","T":"ACG"}
        while q:
            node,step=q.pop(0)
            if node==end:
                return step
            for i,v in enumerate(node):
                for j in dict[v]:
                    new_node=node[:i]+j+node[i+1:]
                    if new_node in bank:
                        q.append((new_node,step+1))
                        bank.remove(new_node)
        return -1
