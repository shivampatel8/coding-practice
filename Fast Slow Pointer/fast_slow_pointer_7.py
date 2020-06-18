def circular_array_loop_exists(arr):
  # TODO: Write your code here
  for i in range(len(arr)):
    slow = i
    fast = i
    current_dir = arr[i]>=0
    while True:
      slow = next(arr, slow, current_dir)
      fast = next(arr, fast, current_dir)
      if fast != -1:
        fast = next(arr, fast, current_dir)
      if slow == -1 or fast == -1 or slow==fast:
        break
    if slow !=-1 and slow==fast:
      return True
  return False

def next(arr, index, current_dir):
  this_dir = arr[index]>=0
  if this_dir!=current_dir:
    return -1
  next_index = (index + arr[index]) % len(arr)
  if next_index == index:
    return -1
  return next_index

def go_back(arr, index):
  if abs(arr[index]) > index:
    remainder = index + arr[index]
    return len(arr) - 1 - remainder
  else:
    return index + arr[index]
def go_forward(arr, index):
  if arr[index] > len(arr) - 1 - index:
    remainder = index - arr[index]
    return abs(remainder) #potential problem
  else:
    return index + arr[index]

def main():
  print(circular_array_loop_exists([1, 2, -1, 2, 2]))
  print(circular_array_loop_exists([2, 2, -1, 2]))
  print(circular_array_loop_exists([2, 1, -1, -2]))


main()
