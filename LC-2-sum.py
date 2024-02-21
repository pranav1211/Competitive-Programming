class Solution(object):
    def twoSum(self, nums, target):
      location = []
      for i in range(len(nums)-1):
        for j in range(len(nums)-1):
          if nums[i]+nums[j+1] == target:
            location.append(i)
            location.append(j+1)
          j+=1
      i+=1
      print(location)

number_list = [2,7,11,1,4,31,36,3,96,36,15,5]
target = 20
solution = Solution()
solution.twoSum(number_list,target)