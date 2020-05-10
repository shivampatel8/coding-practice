#given multiple strings determine the order of the alphabet used in them(strings are sorted)
#eg:['abdeghi','abcdefghi','avbcdefghi']

def main(list_of_strings):
  graph_dict = {}
  for i in list_of_strings:
    x = list(i)
    for j in x:
      graph_dict[j] = []
  pass

if __name__ == '__main__':
  main()