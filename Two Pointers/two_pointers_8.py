def dutch_flag_sort(arr):
  # TODO: Write your code here
  left = 0
  right = len(arr)-1
  length = len(arr)-1
  while left<right:
    print(arr)
    if arr[left]>arr[right]:
      # swap(arr[left],arr[right])
      temp = arr[left]
      arr[left] = arr[right]
      arr[right] = temp
    if arr[left] == 0:
      left+=1
    if arr[right] == 2:
      right-=1
    length-=1
    if length == 0:
      break
  return 

def main():
  arr = [1, 0, 2, 1, 0]
  dutch_flag_sort(arr)
  print(arr)

  arr = [2, 2, 0, 1, 2, 0]
  dutch_flag_sort(arr)
  print(arr)

if __name__ == '__main__':
  main()