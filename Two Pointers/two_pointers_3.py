def make_squares(arr):
  squares = []
  # TODO: Write your code here
  i = 0
  j = len(arr)-1
  while i<=j:
    print(i,j)
    if abs(arr[i]) <= abs(arr[j]):
      squares.insert(0,arr[j]*arr[j])
      j-=1
    else:
      squares.insert(0,arr[i]*arr[i])
      i+=1



  return squares
if __name__ == '__main__':
  print("Squares: " + str(make_squares([-2, -1, 0, 2, 3])))
  print("Squares: " + str(make_squares([-3, -1, 0, 1, 2])))

