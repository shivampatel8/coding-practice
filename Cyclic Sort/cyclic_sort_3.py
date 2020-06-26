def find_missing_numbers(nums):
  # TODO: Write your code here
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] -1
    if nums[i] != nums[j]:
      nums[i] , nums[j] = nums[j], nums[i]
    else:
      i+=1
  return_list = []
  for i in range(len(nums)):
    if i+1 != nums[i]:
      return_list.append( i + 1)
  return return_list
      
def main():
  print(find_missing_numbers([2, 3, 1, 8, 2, 3, 5, 1]))
  print(find_missing_numbers([2, 4, 1, 2]))
  print(find_missing_numbers([2, 3, 2, 1]))


main()