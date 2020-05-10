
def Bag(n, W): 
  if v_list[n]==0 or w_list[n]==0:
    return 0
  elif w_list[n] > W:
    Result = Bag(n-1, W)
  else:
    Temp1 = bag(n-1, W)  
    Temp2 = V_list[n] + Bag(n-1, W - w_list[n])
    return max{Temp1, Temp2}

def main():
  W=4
  w = [3.1111,2,2]
  v = [1.65,1,1]
  Bag(2,W)
  pass