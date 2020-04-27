# 每日练习
## 本周任务
- [x] Two Sum
- [ ] 3sum
- [ ] get-kth-magic-number-lcci
##  4.27周一
### Two Sum
标签：
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
