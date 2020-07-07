from collections import deque
class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        bank=set(bank)
        if end not in bank:
            return -1
        queue=deque()
        queue.append([start,0])
        visited=set()
        char='ACGT'
        
        while queue:
            cur,cnt=queue.popleft()
            if cur==end:
                return cnt
            for i in range(len(cur)):
                for c in char:
                    new=cur[:i]+c+cur[i+1:]
                    if new in bank and new not in visited:
                        visited.add(new)
                        queue.append([new,cnt+1])
       return -1
        
