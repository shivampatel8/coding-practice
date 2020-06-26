def cyclic_sort(nums):
  # TODO: Write your code here
  i=0
  while i < len(nums):
    # print('outside if',nums[i]-1, i)
    if nums[i]-1 != i:
      # print('nums ', nums)
      # print('before swap',nums[i], nums[nums[i]-1])
      index = nums[i]-1
      nums[i], nums[index] = nums[index], nums[i]
      # print('after swap',nums[i], nums[nums[i]-1])
    else:
      i+=1
  return nums

def main():
  print(cyclic_sort([3, 1, 5, 4, 2]))
  print(cyclic_sort([2, 6, 4, 3, 1, 5]))
  print(cyclic_sort([1, 5, 6, 4, 3, 2]))


main()