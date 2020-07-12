class Solution:
    def mySqrt(self, x: int) -> int:
        if x==0:
            return 0
        left,right=1,x//2
        while left<right:
            mid=(left+right+1)>>1
            square=mid*mid
            if square>x:
                right=mid-1
            else:
                left=mid
        return left
