
def longest_substring_with_k_distinct(str1, k):
	distict_char = {}
	starting_index = 0
	maxlen = 0
	for ending_index in range(len(str1)):
		distict_char[str1[ending_index]] = distict_char[str1[ending_index]] + 1 if str1[ending_index] in distict_char.keys() else 1
		while len(distict_char.keys()) > k:
			distict_char[str1[starting_index]] = distict_char[str1[starting_index]] - 1
			if distict_char[str1[starting_index]] == 0 : del distict_char[str1[starting_index]] 
			starting_index +=1
		maxlen = max(maxlen,(ending_index - starting_index)+1)
	return maxlen

if __name__ == '__main__':
	str1 = 'cbbebi'
	k = 2
	print (longest_substring_with_k_distinct(str1,k))
