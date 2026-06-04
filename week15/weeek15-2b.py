#week15-2b.py
#1143.
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        M,N=len(text1),len(text2)
        table=[[0]*(N+1) for i in range(M+1)]
        for i in range(M):
            for j in range(N):
                #case1=table[i-1][j]
                #case2=table[i-1][j]
                #case3=table[i-1][j]
                if text1[i]==text2[j]:table[i+1][j+1]=table[i][j]+1
                table[i+1][j+1]=max(table[i+1][j+1],table[i][j+1],table[i+1][j])
        return table[M][N]
