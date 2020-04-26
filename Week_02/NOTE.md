# 第二周复习笔记
> 借助哈希表来解题
##  两个数组的交集
``` python
@requires_authorization
def somefunc(param1='', param2=0):
    '''A docstring'''
    if param1 > param2: # interesting
        print 'Greater'
    return (param2 - param1 + 1) or None
class SomeClass:
    pass
>>> message = '''interpreter
... prompt'''
```
##  HashMap小总结
### 散列思想
    必备：键（key）或者关键字
         散列函数-将key转化为数组下标的映射方法
         散列值-散列函数计算得到的值
    值得注意的点：散列表用的就是数组支持按照下标随机访问的时候，时间复杂度是 O(1) 的特性。我们通过散列函数把元素的键值映射为下标，然后将数据存储在数组中对应下标的位置。当我们按照键值查询元素时，我们用同样的散列函数，将键值转化数组下标，从对应的数组下标的位置取数据
    散列函数设计的基本要求：
    1、散列函数计算得到的散列值是一个非负整数；
    2、如果 key1 = key2，那 hash(key1) == hash(key2)；
    3、如果 key1 ≠ key2，那 hash(key1) ≠ hash(key2)。
### 如何解决散列冲突
    开放寻址法（open addressing）和链表法（chaining）
