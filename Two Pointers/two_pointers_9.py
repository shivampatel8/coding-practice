def search_quadruplets(arr, target):
  quadruplets = []
  arr.sort()
  for i in range(len(arr)-3):
    if i > 0 and arr[i] == arr[i-1]:
      continue
    # for j in range(i+1,len(arr)-2):
    #   if j > i + 1 and arr[j] == arr[j - 1]:
    #     continue
    search_triplets(arr,target-arr[i],i+1,quadruplets,arr[i])
  return quadruplets

def search_triplets(arr,target_sum,left,quadruplets,cur_num):
  for i in range(len(arr)):
  # while left<right:
    if i > 0 and arr[i] == arr[i-1]:
      continue
    search_pairs(arr,target_sum-arr[i],i+1,quadruplets,cur_num, arr[i])
  return quadruplets

def search_pairs(arr, target_sum, left, quadruplets,cur_num,cur_num1):
  right = len(arr) -1
  while left<right:
    current_sum = arr[left] + arr[right]
    if current_sum==target_sum:
      # print(cur_num1,cur_num,arr[left],arr[right])
      quadruplets.append((cur_num,cur_num1,arr[left],arr[right]))
      left+=1
      right-=1
      while left < right and arr[left] == arr[left-1]:
        left+=1
      while left < right and arr[right] == arr[right+1]:
        right-=1
    elif current_sum < target_sum:
      left+=1
    else:
      right-=1

def main():
  print(search_quadruplets([4, 1, 2, -1, 1, -3], 1))
  print(search_quadruplets([2, 0, -1, 1, -2, 2], 2))

if __name__ == '__main__':
  main()