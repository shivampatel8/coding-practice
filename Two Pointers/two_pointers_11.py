import math
def shortest_window_sort(arr):
  # TODO: Write your code here
  left, right = 0, len(arr)-1
  while(left<len(arr)-1 and arr[left]<=arr[left+1]):
    left += 1
  if left == len(arr)-1:
    return 0
  while(right>0 and arr[right]>=arr[right-1]):
    right-=1

  max_subarray = -math.inf
  min_subarray = math.inf
  for i in range(left,right):
    max_subarray = max(max_subarray,arr[i])
    min_subarray = min(min_subarray,arr[i])
  while(left>0 and arr[left-1]>min_subarray):
    left-=1
  while(right<len(arr)-1 and arr[right+1]<max_subarray):
    right+=1
  return right - left + 1


def main():
  print(shortest_window_sort([1, 2, 5, 3, 7, 10, 9, 12]))
  print(shortest_window_sort([1, 3, 2, 0, -1, 7, 10]))
  print(shortest_window_sort([1, 2, 3]))
  print(shortest_window_sort([3, 2, 1]))

if __name__ == '__main__':
  main()