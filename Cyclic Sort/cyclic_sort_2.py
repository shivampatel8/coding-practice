def find_missing_number(nums):
  # TODO: Write your code here
  i, n = 0, len(nums)
  while i < n:
    j = nums[i]
    if nums[i] < n and nums[i] != nums[j]:
      nums[i] , nums[j] = nums[j], nums[i]
    else:
      i+=1
  print(nums)
  for i in range(len(nums)):
    if i != nums[i]:
      return i
      
def main():
  print(find_missing_number([4, 0, 3, 1]))
  print(find_missing_number([8, 3, 5, 2, 4, 6, 0, 1]))


main()