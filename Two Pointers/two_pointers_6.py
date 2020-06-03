def triplet_with_smaller_sum(arr, target):
  count = 0
  # TODO: Write your code here
  arr.sort()
  for i in range(len(arr)-2):
    count+=search_pair(arr,target - arr[i],i)
  return count

def search_pair(arr, target, first):
  count = 0
  left = first + 1
  right = len(arr) - 1
  while left < right:
    if arr[left] + arr[right] < target:
      count+= right-left
      left+=1
    else:
      right-=1
  return count

def main():
  print(triplet_with_smaller_sum([-1, 0, 2, 3], 3))
  print(triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5))

if __name__ == '__main__':
  main()
