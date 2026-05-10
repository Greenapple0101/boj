class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        cnt={}

        for ch in s:
            cnt[ch]=cnt.get(ch,0)+1

        for ch in t:
            if ch not in cnt:
                return False
            
            cnt[ch]-=1

            if cnt[ch]<0:
                return False
        
        return True
