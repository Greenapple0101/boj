class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict1={}
        for i,numi in enumerate(nums):
            for j, numj in enumerate(nums):
                if i==j:continue
                if (numi+numj==target):
                    return [i,j]