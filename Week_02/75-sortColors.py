from typing import List
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def swap(nums,index1,index2):
            nums[index1],nums[index2]=nums[index2],nums[index1]
        size=len(nums)
        if size<2:
            return
        i=0
        zero=0
        two=size
        while i<two:
            if nums[i]==0:
                swap(nums,0,i)
                i+=1
                zero+=1
            elif nums[i]==1:
                i+=1
            else:
                two-=1
                swap(nums,i,two)
