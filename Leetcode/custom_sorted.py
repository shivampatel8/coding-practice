#6,3,4,5

def main(arr):
  i = 0
  j = len(arr)-1
  ready_to_swap_odd = False
  ready_to_swap_even = False
  number_of_swap = 0
  while i<j:
    if arr[i]%2!=0:
      ready_to_swap_odd = True
    else:
      i+=1
    if arr[j]%2==0:
      ready_to_swap_even = True
    else:
      j-=1
    if ready_to_swap_odd and ready_to_swap_even:
      number_of_swap+=1
      i+=1
      j-=1
      ready_to_swap_odd = False
      ready_to_swap_even = False
  return number_of_swap

if __name__ == '__main__':
  print(main([13,10,21,20]))