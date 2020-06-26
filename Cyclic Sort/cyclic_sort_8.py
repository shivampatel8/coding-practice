def find_first_k_missing_positive(nums, k):
  missingNumbers = []
  # TODO: Write your code here
  i, n = 0, len(nums)
  while i < n:
    j = nums[i] - 1
    if nums[i] > 0:
      if nums[i] > 0 and nums[i] <= n and nums[i] != nums[j]:
        nums[i] , nums[j] = nums[j], nums[i]
      else:
        i+=1
    else: 
      i+=1
  extraNumbers = set()
  for i in range(len(nums)):
    if len(missingNumbers)<k:
      if i+1 != nums[i]:
        missingNumbers.append(i+1)
        extraNumbers.add(nums[i])
  i = 1
  while len(missingNumbers)<k:
    candidate_number = i+n
    if candidate_number not in extraNumbers:
      missingNumbers.append(candidate_number)
    i+=1

  return missingNumbers


def main():
  # print(find_first_k_missing_positive([3, -1, 4, 5, 5], 3))
  print(find_first_k_missing_positive([2, 3, 4], 3))
  # print(find_first_k_missing_positive([-2, -3, 4], 2))


main()