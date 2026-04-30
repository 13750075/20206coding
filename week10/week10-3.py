#week10-3.py
#1448
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans=0
        def helper(root,big):
            if root==None:return 0
            ans=0
            if root.val>=big:
                ans+=1
                big=root.val
            ans+=helper(root.left,big)
            ans+=helper(root.right,big)
            return ans
        return helper(root,0)
