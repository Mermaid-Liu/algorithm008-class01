# 知识点总结：
##  Recursion[递归]
    定义：通过函数来进行的循环
    * 向下进入到不同的层，又向上回到之前的那一层
    *参数在函数不同层之间传递变量
### 代码模版
``` python
class Solution:
    def recursion(level,param1,param2...):
        #递归终止条件
        if level>MAX_LEVEL:
        process_result
        return
        #处理当前层逻辑
        process(level,data...)
        #下探到下一层
        self.recursion(level+1,p1,p2...)
        #清理当前层
```
##  三个思维要点：
1.不要人肉进行递归
2.找到最近最简的方法，将其拆解成可重复解决的问题（重复子问题）
3.数学归纳思维

# 每日练习
## 本周任务(每日一题)
- [x] 1-Two Sum
- [x] 15-3sum
- [ ] 面试题 17.09. 第 k 个数
## 实战练习
- [x] 70
- [ ] 22
- [ ] 226
- [ ] 98
- [ ] 104
- [ ] 111
- [ ] 297
## 本周作业
- [x] 1-Two Sum
- [x] 15-3sum
- [ ] get-kth-magic-number-lcci
##  4.27周一
### Two Sum
标签：哈希表（字典）
> 之前的实现都是用的javascript，这次用的python，学了python的enumerate()方法，这个方法可以直接达到hashmap的效果；两个数的和是target，因此先便利一遍，把整个数组的值都放到一个字典里，之后再便利一遍，如果target减去每一项，差也在这个dictionary里的话，就可以输出出来了。
### Code block
``` python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap={}
        for ind,num in enumerate(nums):
            hashmap[num]=ind
        for i,num in enumerate(nums):
            j=hashmap.get(target-num)
            if j is not None and i!=j:
                return [i,j]
```
### 3Sum
标签：排序➕双指针
> 现将原数组排序好，然后利用双指针，将当前值与当前值加一和末尾值做和
corner case：当数组为空或者数组的长度小于3的时候，返回[]
initialize：left=i+1 right=len(nums)-1
三种情况：1）当sum<0时：left++
2)当sum>0时，right--
3)当sum=0时，append到数组里
当right和left重合或者left>right时，i++
### CodeBlock
```
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        if not nums or n<3:
            return []
        res=[]
        nums.sort()
        for i in range(n):
            if nums[i]>0:
                return res
            if i>0 and nums[i]==nums[i-1]:
                continue
            L=i+1
            R=n-1
            while(L<R):
                if(nums[i]+nums[L]+nums[R]==0):
                    res.append([nums[i],nums[L],nums[R]])
                    while(L<R and nums[L]==nums[L+1]):
                        L=L+1
                    while(L<R and nums[R]==nums[R-1]):
                        R=R-1
                    L=L+1
                    R=R-1
                elif(nums[i]+nums[L]+nums[R]<0):
                    L=L+1
                else:
                    R=R-1
        return res
```
##  4.28周二
### 实战项目-爬楼梯
>   先找到重复子问题，用数学归纳法总结出来递推公式，再借助动态规划的思想完成这道题目
```
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=2:
            return n
        f1,f2,f3=1,2,3
        for i in range(3,n+1):
            f3=f1+f2
            f1=f2
            f2=f3
        return f3
       ```
