def remove_duplicates(arr):
  # TODO: Write your code here
  j = 1
  i = 1
  while i < len(arr):
    if arr[j-1] != arr[i]:
      arr[j] = arr[i]
      j+=1
    i+=1
  # print(j)
  return j

if __name__ == '__main__':
  print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))
  print(remove_duplicates([2, 2, 2, 11]))
