class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp=[[1 for x in range(n)]for x in range(m)]
        print(dp)
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j]=dp[i][j-1]+dp[i-1][j]
        return dp[-1][-1]
