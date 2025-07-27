class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic1={} #number,index
        for index,value in enumerate(nums): 
            requiredNum = target-value
            if requiredNum in dic1:
                return [index,dic1[requiredNum]]
            
            dic1[value]=index
