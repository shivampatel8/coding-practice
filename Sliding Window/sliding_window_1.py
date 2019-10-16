#Given an array, find the average of all subarrays of size ‘K’ in it.

def find_average():
	pass

def average_subarrays(array, k):
	list_of_results = []
	window_start = 0
	window_sum = 0.0
	for window_end in range(len(array)):
		window_sum += array[window_end]
		
		if window_end>=k-1:
			
			list_of_results.append((window_sum/k))
			window_sum-=array[window_start]
			window_start+=1
	return list_of_results

if __name__ == '__main__':
	array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
	k = 5
	list_averages = average_subarrays(array, k)
	print( list_averages)