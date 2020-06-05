def find_happy_number(num):
  slow, fast = num, num
  while fast != 1 and next(fast) != 1 :
    slow = next(slow)
    fast = next(next(fast))
    if slow == fast:
      return False
  return True

def next(num):
  num_list = [int(d) for d in str(num)]
  cal_number = 0
  for i in num_list:
    cal_number += pow(i,2)
  return cal_number


def main():
  print(find_happy_number(23))
  print(find_happy_number(12))


main()