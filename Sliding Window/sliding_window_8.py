def length_of_longest_substring_efficient(arr,k):
  window_start = 0
  max_length = 0
  max_repeat_letter_count = 0
  max_letter = 0
  char_index_map = {}
  for window_end in range(len(arr)):
    right_char = arr[window_end]
    char_index_map[right_char] = 1 if right_char not in char_index_map.keys() else char_index_map[right_char]+1
    max_letter = max(max_letter,char_index_map[right_char])
    letter_sum = window_end - window_start + 1
    if letter_sum - max_letter>k:
      char_index_map[arr[window_start]]-=1
      if char_index_map[arr[window_start]] == 0:
        del char_index_map[arr[window_start]]
      window_start +=1 
    # char_index_map[right_char] = window_end
    max_length = max(max_length, window_end - window_start + 1)
  return max_length

def main():
  # print("Length of the longest substring: " + str(length_of_longest_substring("aabccbb",2)))
  # print("Length of the longest substring: " + str(length_of_longest_substring("abbcb",1)))
  # print("Length of the longest substring: " + str(length_of_longest_substring("abccde",1)))
  print("Length of the longest substring: " + str(length_of_longest_substring_efficient([0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1],2)))
  print("Length of the longest substring: " + str(length_of_longest_substring_efficient([0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1],3)))
  # print("Length of the longest substring: " + str(length_of_longest_substring_efficient("abccde",1)))

if __name__ == '__main__':
  main()
