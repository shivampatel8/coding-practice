from __future__ import print_function

class Interval:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def print_interval(self):
        print("[" + str(self.start) + ", " + str(self.end) + "]", end='')

def insert(intervals, new_interval):
  merged = []
  i, start, end = 0, 0, 1
  while i < len(intervals) and intervals[i].end < new_interval.start:
    merged.append(intervals[i])
    i+=1

  while  i < len(intervals) and intervals[i].start <= new_interval.end:
    new_interval.start = min(intervals[i].start, new_interval.start)
    new_interval.end = max(intervals[i].end, new_interval.end)
    i += 1

  merged.append(new_interval)
  while i<len(intervals):
    merged.append(intervals[i])
    i += 1
  return merged

def find_employee_free_time(schedule):
    result = []
    intervals = schedule[0]
    for i in range(1,len(schedule)):
        for j in range(len(schedule[i])):
            intervals = insert(intervals,schedule[i][j])
    for i in range(len(intervals)-1):
        result.append(Interval(intervals[i].end, intervals[i+1].start))
    # TODO: Write your code here
    return result

def find_employee_free_time_heap(schedule):
    if schedule is None:
        return []

    n = len(schedule)
    result, minHeap = [], []

    # insert the first interval of each employee to the queue
    for i in range(n):
        heappush(minHeap, EmployeeInterval(schedule[i][0], i, 0))

    previousInterval = minHeap[0].interval
    while minHeap:
        queueTop = heappop(minHeap)
        # if previousInterval is not overlapping with the next interval, insert a free interval
        if previousInterval.end < queueTop.interval.start:
            result.append(Interval(previousInterval.end,
                                   queueTop.interval.start))
            previousInterval = queueTop.interval
        else:  # overlapping intervals, update the previousInterval if needed
            if previousInterval.end < queueTop.interval.end:
                previousInterval = queueTop.interval

        # if there are more intervals available for the same employee, add their next interval
        employeeSchedule = schedule[queueTop.employeeIndex]
        if len(employeeSchedule) > queueTop.intervalIndex + 1:
            heappush(minHeap, EmployeeInterval(employeeSchedule[queueTop.intervalIndex + 1], queueTop.employeeIndex,
                                               queueTop.intervalIndex + 1))

    return result

def main():

    input = [[Interval(1, 3), Interval(5, 6)], [
        Interval(2, 3), Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3), Interval(9, 12)], [
        Interval(2, 4)], [Interval(6, 8)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()

    input = [[Interval(1, 3)], [
        Interval(2, 4)], [Interval(3, 5), Interval(7, 9)]]
    print("Free intervals: ", end='')
    for interval in find_employee_free_time(input):
        interval.print_interval()
    print()


main()
