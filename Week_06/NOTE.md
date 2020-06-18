# 动态规划Dynamic Programming
## Review 分治算法
```
def divide_conqur(problem,param1,param2...):
  if problem is None:
    #递归终止条件
    print_result
    return
  #拆分子问题
  data=prepare_data(problem)
  subproblems=split.problem(problem,data)
  #调子问题的递归函数
  subresult1=self.divide_conquer(subproblems[0],p1,...)
  subresult2=self.divide_conquer(subproblems[1],p2,...)
  ...
  #合并结果
  result=process_result(subresult1,subresult2...)
```
## Review 递归算法
```
Public void recur(level,param){
  if(level>MAX_LEVEL){
  #递归终止条件
    return
  }
  process(level,param)//处理当前层逻辑
  recur(level:level+1,newParam)//下探到下一层
}
```
## 动态规划概念
#### 动态规划=分治+最优子结构
#### 本质：寻找重复性->计算机指令集
## 动态规划与递归

## 动态规划技巧
