def length_of_longest_substring(str,k):
  window_start = 0
  max_length = 0
  max_repeat_letter_count = 0
  char_index_map = {}
  for window_end in range(len(str)):
    right_char = str[window_end]
    char_index_map[right_char] = 1 if right_char not in char_index_map.keys() else char_index_map[right_char]+1
    max_letter,letter_sum = max_letter_dict(char_index_map)
    if letter_sum - max_letter>k:
      char_index_map[str[window_start]]-=1
      if char_index_map[str[window_start]] == 0:
        del char_index_map[str[window_start]]
      window_start +=1 
    # char_index_map[right_char] = window_end
    max_length = max(max_length, window_end - window_start + 1)
  return max_length

def max_letter_dict(char_dict):
  max_letter = -1
  letter_sum = 0
  for key in char_dict.keys():
    letter_sum += char_dict[key]
    max_letter = max(max_letter,char_dict[key])
  return max_letter,letter_sum

#efficient way
def length_of_longest_substring_efficient(str,k):
  window_start = 0
  max_length = 0
  max_repeat_letter_count = 0
  max_letter = 0
  char_index_map = {}
  for window_end in range(len(str)):
    right_char = str[window_end]
    char_index_map[right_char] = 1 if right_char not in char_index_map.keys() else char_index_map[right_char]+1
    max_letter = max(max_letter,char_index_map[right_char])
    letter_sum = window_end - window_start + 1
    if letter_sum - max_letter>k:
      char_index_map[str[window_start]]-=1
      if char_index_map[str[window_start]] == 0:
        del char_index_map[str[window_start]]
      window_start +=1 
    # char_index_map[right_char] = window_end
    max_length = max(max_length, window_end - window_start + 1)
  return max_length

def main():
  # print("Length of the longest substring: " + str(length_of_longest_substring("aabccbb",2)))
  # print("Length of the longest substring: " + str(length_of_longest_substring("abbcb",1)))
  # print("Length of the longest substring: " + str(length_of_longest_substring("abccde",1)))
  print("Length of the longest substring: " + str(length_of_longest_substring_efficient("aabccbb",2)))
  print("Length of the longest substring: " + str(length_of_longest_substring_efficient("abbcb",1)))
  print("Length of the longest substring: " + str(length_of_longest_substring_efficient("abccde",1)))

if __name__ == '__main__':
  main()
