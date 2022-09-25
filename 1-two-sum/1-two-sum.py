class Solution:
    def twoSum(self, nums, target):
        
        new_list = {}
        for i in range(len(nums)):
            if nums[i] in new_list: 
                return [i,new_list[nums[i]]]
            x = target - nums[i]
            new_list[x] = i
        
            
#             for j in range(len(nums)):
#                 if nums[i] + nums[j] == target:
#                     new_list.append(i)
#                     new_list.append(j)
        
#         return new_list
                
        
        
        
        