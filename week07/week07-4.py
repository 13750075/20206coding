#week07-4.py
#394.
class Solution:
    def decodeString(self, s: str) -> str:
        ans=[]
        nowN,nowS=0,''
        for c in s:
            if c.isdigit():
                nowN=nowN*10+int(c)
            elif c.isalpha():
                nowS+=c
            elif c=='[':
                ans.append((nowN,nowS))
                nowN,nowS=0,''
            elif c==']':
                prevN,prevS=ans.pop()
                nowS=prevS+prevN*nowS
        return nowS
