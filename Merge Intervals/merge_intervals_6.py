from heapq import *


class job:
  def __init__(self, start, end, cpu_load):
    self.start = start
    self.end = end
    self.cpu_load = cpu_load

  def __lt__(self, other):
    # min heap based on meeting.end
    return self.end < other.end

def find_max_cpu_load(meetings):
  # TODO: Write your code here
  meetings.sort(key=lambda x: x.start)

  max_cpu_load = 0
  minHeap = []
  current_cpu_load = 0
  for meeting in meetings:
    # remove all the meetings that have ended
    while(len(minHeap) > 0 and meeting.start >= minHeap[0].end):
      popped = heappop(minHeap)
      current_cpu_load -= popped.cpu_load
    # add the current meeting into min_heap
    heappush(minHeap, meeting)
    current_cpu_load += meeting.cpu_load

    # all active meetings are in the min_heap, so we need rooms for all of them.
    max_cpu_load = max(max_cpu_load, current_cpu_load)
  return max_cpu_load


def main():
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 3), job(2, 5, 4), job(7, 9, 6)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(6, 7, 10), job(2, 4, 11), job(8, 12, 15)])))
  print("Maximum CPU load at any time: " + str(find_max_cpu_load([job(1, 4, 2), job(2, 4, 1), job(3, 6, 5)])))


main()
