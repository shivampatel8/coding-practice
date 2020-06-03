def backspace_compare(str1, str2):
  end_str1 = len(str1)-1
  end_str2 = len(str2)-1
  hash1 = len(str1)-1
  hash2 = len(str2)-1
  while hash1>=0 and hash2>=0:
    # print(str1[hash1],str2[hash2])
    if str1[end_str1]=='#':
      # print('here1')
      while str1[end_str1] == '#':
        # print(end_str1,end_str2)
        end_str1-=1
        hash1-=2
    if str2[end_str2]=='#':
      # print('here2')
      while str2[end_str2] == '#':
        # print(end_str1,end_str2)
        end_str2-=1
        hash2-=2
    # print(str1[hash1],str2[hash2],hash1,hash2)
    if str1[hash1]!=str2[hash2]:
      return False
    else:
      hash1-=1
      hash2-=1
      end_str1-=1
      end_str2-=1


  return True


def main():
  print(backspace_compare("xy#z", "xzz#"))
  print(backspace_compare("xy#z", "xyz#"))
  print(backspace_compare("xp#", "xyz##"))
  print(backspace_compare("xywrrmp", "xywrrmu#p"))
if __name__ == '__main__':
  main()