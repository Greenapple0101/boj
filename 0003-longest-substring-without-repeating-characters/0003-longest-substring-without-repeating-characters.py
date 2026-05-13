class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last={}
        ans=0
        left=0
        for right,ch in enumerate(s):
            if ch in last and last[ch]>=left:
                left=last[ch]+1
            else:
                ans=max(ans,right-left+1)

            last[ch]=right
        return ans