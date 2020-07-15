class Solution:
    def mySqrt(self, x: int) -> int:
        if x<2:
            return x
        left,right=1,x//2
        while left<right:
            mid=(left+right+1)>>1
            if mid*mid>x:
                right=mid-1
            else:
                left=mid
        return left
