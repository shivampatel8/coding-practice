def main():
  a = [2,2,3,4,3,3,2,2,1,1,2,5]
  current_number = -1
  peak = False
  no_castle = 0
  for i in a:
    if i == current_number:
      continue
    if i>current_number:
      peak = True
    if peak == True:
      

