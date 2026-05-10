class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dictt={}

        for i,num in enumerate(nums):
            need=target-num

            if need in dictt:
                return (dictt[need],i)
            
            dictt[num]=i