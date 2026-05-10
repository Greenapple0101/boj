class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        dictt={}

        for i,num in enumerate(nums):

            if num not in dictt:
                dictt[num]=i
            else:
                return True
        
        return False


            
