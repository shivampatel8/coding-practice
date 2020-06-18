def merge(intervals_a, intervals_b):
  result = []
  i = 0
  j = 0
  while True:
    if is_intersecting(intervals_a[i], intervals_b[j]):
      start = max(intervals_a[i][0],intervals_b[j][0])
      end = min(intervals_a[i][1],intervals_b[j][1])
      if intervals_a[i][1] != intervals_b[j][1]:
        if end == intervals_a[i][1]:
          i+=1
        else:
          j+=1
      else:
        i+=1
        j+=1
      result.append([start,end])
    else:
      if intervals_a[i][1]<intervals_b[j][1]:
        i+=1
      else:
        j+=1
    if i == len(intervals_a) or j == len(intervals_b):
      break
  # TODO: Write your code here
  return result

def is_intersecting(interval_a, interval_b):
  if (interval_a[0]<=interval_b[1] and interval_a[0]>=interval_b[0]) or (interval_b[0]<=interval_a[1] and interval_b[0]>=interval_a[0]):
    return True
  else:
    return False

def main():
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 6], [7, 9]], [[2, 3], [5, 7]])))
  print("Intervals Intersection: " + str(merge([[1, 3], [5, 7], [9, 12]], [[5, 10]])))


main()
