def max_sub_array_size_k(arr, k):
	max_sum = 0
	window_sum = 0
	window_start = 0
	for window_end in range(len(arr)):
		window_sum+=arr[window_end]
		if window_end>= k-1:
			max_sum = max(max_sum,window_sum)
			window_sum-=arr[window_start]
			window_start+=1
	return max_sum
	

if __name__ == '__main__':
	arr = [2, 1, 5, 1, 3, 2]
	k = 3
	max_sum = max_sub_array_size_k(arr,k)
	print( max_sum)
	
	arr = [2, 3, 4, 1, 5]
	k = 2
	max_sum = max_sub_array_size_k(arr,k)
	print( max_sum)