class one:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(0,len(nums)):
            for j in range(len(nums)):
                if nums[i]+nums[j]==target:
                    return(i,j)
    def Twosum(self,nums:list[int],target: int) -> list[int]:
        for i in range(0,len(nums)):
            j=target-nums[i]
            if j in nums:
                return(i,nums.index(j))

arr=[1,2,3,4,5,6,7,8,9,0]
print(one.twoSum(1,arr,15))
print(one.Twosum(1,arr,13))