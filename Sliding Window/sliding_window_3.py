import math
def sub_array_sum(arr, s):
	window_sum = 0
	starting_index = 0
	sub_array_length = math.inf
	for ending_index in range(len(arr)):
		window_sum+=arr[ending_index]
		while window_sum>=s:
			sub_array_length = min(sub_array_length,(ending_index-starting_index)+1)
			window_sum-=arr[starting_index]
			starting_index+=1

	return sub_array_length if sub_array_length != math.inf else 0 
if __name__ == '__main__':
	arr = [2, 1, 5, 2, 3, 2]
	s = 7
	print(sub_array_sum(arr,s))