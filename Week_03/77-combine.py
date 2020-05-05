class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        def back(candidates,cur):
            if len(cur)==k:
                result.append(cur[:])
                return
            for i in range(len(candidates)):
                if len(cur)>0 and candidates[i]<cur[-1]:
                    continue
                cur.append(candidates[i])
                back(candidates[:i]+candidates[i+1:],cur)
                cur.pop()
        nums=[i for i in range(1,n+1)]
        result=[]
        back(nums,[])
        return result
