def find_all_duplicates(nums):

  # TODO: Write your code here

  i, n = 0, len(nums)
  while i < n:
    j = nums[i] -1
    if nums[i] != nums[j]:
      nums[i] , nums[j] = nums[j], nums[i]
    else:
      i+=1
  duplicateNumbers = []
  for i in range(len(nums)):
    if i+1 != nums[i]:
      duplicateNumbers.append(nums[i])
  return duplicateNumbers


def main():
  print(find_all_duplicates([3, 4, 4, 5, 5]))
  print(find_all_duplicates([5, 4, 7, 2, 3, 5, 3]))


main()