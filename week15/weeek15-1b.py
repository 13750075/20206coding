#week15-1b.py
#62.
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table=[[0]*n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if i==0:table[i][j]=1
                elif j==0:table[i][j]=1
                else: table[i][j]=table[i-1][j]+table[i][j-1]
        return table[m-1][n-1]
