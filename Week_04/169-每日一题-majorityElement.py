class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        def helper(lo,hi):
            if lo==hi:
                return nums[lo]
            mid=(hi-lo)//2+lo
            left=helper(lo,mid)
            right=helper(mid+1,hi)

            if left==right:
                return left
            left_count=sum(1 for i in range(lo,hi+1) if nums[i]==left)
            right_count=sum(1 for i in range(lo,hi+1) if nums[i]==right)
            return left if left_count>right_count else right
        return helper(0,len(nums)-1)
