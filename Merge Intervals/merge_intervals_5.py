from heapq import *


class Meeting:
  def __init__(self, start, end):
    self.start = start
    self.end = end

  def print_interval(self):
    print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

  def __repr__(self):
    return str([self.start,self.end])

def min_meeting_rooms(meetings):
  count = 1
  room_count = 1
  meetings.sort(key=lambda x: x.start)
  print(meetings)
  start = meetings[0].start
  end = meetings[0].end
  for i in range(1, len(meetings)):
    interval = meetings[i]
    if interval.start< end:
      count+=1
      start = max(interval.start,start)
      end = min(interval.end,end)
    else:
      room_count = max(room_count,count)
      count=1
      start = interval.start
      end = interval.end
  return max(room_count,count)


def main():
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 5), Meeting(7, 9)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(6, 7), Meeting(2, 4), Meeting(8, 12)])))
  print("Minimum meeting rooms required: " +
        str(min_meeting_rooms([Meeting(1, 4), Meeting(2, 3), Meeting(3, 6)])))
  print("Minimum meeting rooms required: " + str(min_meeting_rooms(
    [Meeting(4, 5), Meeting(2, 3), Meeting(2, 4), Meeting(3, 5)])))



main()
