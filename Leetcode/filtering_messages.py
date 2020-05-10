def filteringMessage(messageA,messageB,messageC):
  # if messageC in messageA and messageC in messageB:
  #   return 0
  backtrack('',messageA,messageB,0,messageC)
  pass
count = 0
flag = False 
def backtrack(string, stringA, stringB, depth, stringC):
  global count
  global flag
  if flag:
    return
  if string == stringB:
    flag = True
    count+=1
  if len(string) == len(stringA):
    if not check_for_virus(string, stringC):
      if string == stringA:
        return 0
      count+=1
    return 0
  lowChar = stringA[depth]

  if depth > 0:
    if stringA[depth-1]==stringB[depth-1]:
      highChar = stringB[depth]
    else:
      highChar = 'z'
  else:
    highChar = stringB[depth]


  for i in range(ord(lowChar),ord(highChar)+1):
  # for i in range(ord(lowChar),ord('z')+1):
    string+=chr(i)
    print(string)
    if stringC in string:
      return
    backtrack(string,stringA,stringB,depth+1,stringC)
    string = string[0:len(string)-1]

def check_for_virus(message, virus):
  if virus in message:
    print('message')
    print('here')
  return virus in message

if __name__ == '__main__':
  filteringMessage('abazfa','abzghz','y')
  # filteringMessage('aa','da','c')
  # filteringMessage('aa','bb','c')
  # filteringMessage('aba','adz','z')
  print (count)

# public List<List<Integer>> subsets(int[] nums) {
#     List<List<Integer>> list = new ArrayList<>();
#     Arrays.sort(nums);
#     backtrack(list, new ArrayList<>(), nums, 0);
#     return list;
# }

# private void backtrack(List<List<Integer>> list , List<Integer> tempList, int [] nums, int start){
#     list.add(new ArrayList<>(tempList));
#     for(int i = start; i < nums.length; i++){
#         tempList.add(nums[i]);
#         backtrack(list, tempList, nums, i + 1);
#         tempList.remove(tempList.size() - 1);
#     }
# }