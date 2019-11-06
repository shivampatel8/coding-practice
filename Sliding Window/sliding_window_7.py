def length_of_longest_substring(str,k):
  window_start = 0
  max_length = 0
  char_index_map = {}
  for window_end in range(len(str)):
    right_char = str[window_end]
    print(right_char)
    print(len(char_index_map.keys())) 
    if len(char_index_map.keys())>k:
      window_start = max(window_start, char_index_map[right_char] + 1)
      char_index_map[window_start]-=1
    char_index_map[str[window_end]] = window_end
    max_length = max(max_length, window_end - window_start + 1)
  return max_length


def main():
  print("Length of the longest substring: " + str(length_of_longest_substring("aabccbb",2)))
  # print("Length of the longest substring: " + str(length_of_longest_substring("abbbb")))
  # print("Length of the longest substring: " + str(length_of_longest_substring("abccde")))


main()
