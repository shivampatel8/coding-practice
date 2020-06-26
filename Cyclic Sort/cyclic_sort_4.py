def find_duplicate(nums):
  # TODO: Write your code here
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] -1
    if nums[i] != nums[j]:
      nums[i] , nums[j] = nums[j], nums[i]
    else:
      i+=1
  print(nums)
  for i in range(len(nums)):
    if i+1 != nums[i]:
      return nums[i]

def main():
  print(find_duplicate([1, 4, 4, 3, 2]))
  print(find_duplicate([2, 1, 3, 3, 5, 4]))
  print(find_duplicate([2, 4, 1, 4, 4]))


main()