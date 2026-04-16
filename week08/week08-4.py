#week08-4.py
#2300.
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        ans=[]
        for spell in spells:
            now=len(potions)-bisect_left(potions,success/spell)
            ans.append(now)
        return ans
