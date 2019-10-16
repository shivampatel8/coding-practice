def fruits_into_baskets(fruits):
  distinct_char = {}
  max_fruits = 0
  starting_index = 0
  for ending_index in range(len(fruits)):
  	distinct_char[fruits[ending_index]] = distinct_char[fruits[ending_index]] + 1 if fruits[ending_index] in distinct_char.keys() else 1
  	while len(distinct_char.keys())>2:
  		distinct_char[fruits[starting_index]] = distinct_char[fruits[starting_index]] - 1
  		if distinct_char[fruits[starting_index]] == 0:
  			del distinct_char[fruits[starting_index]]
  		starting_index+=1
  	max_fruits = max(max_fruits,(ending_index-starting_index)+1)
  return max_fruits
  
if __name__ == '__main__':
	fruits = ['A', 'B', 'C', 'A', 'C']
	print(fruits_into_baskets(fruits))