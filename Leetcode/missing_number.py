class Solution:
    def missingNumber(self, nums) -> int:
        x = sum(nums)
        y = len(nums)
        return ((y*(y+1))/2)-x

    def missingNumber1(self, nums) -> int:
        y = len(nums)
        for i,index in enumerate(nums):
          y^=i^index
        return y
if __name__ == '__main__':
  print(Solution().missingNumber1([0,1,2,3,4,5,6,7,9]))