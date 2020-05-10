def pair_with_targetsum(arr, target_sum):
  # TODO: Write your code here
  i = 0
  j = len(arr)-1
  while j>i:
    if arr[i]+arr[j] == target_sum:
      return[i, j]
    elif arr[i]+arr[j] > target_sum:
      j-=1
    else:
      i+=1

  return [-1, -1]

if __name__ == '__main__':
  print(pair_with_targetsum([1, 2, 3, 4, 6],6))
  print(pair_with_targetsum([2, 5, 9, 11],11))
