# your code goes here
import copy
W = 6.11
w = [1,3,2,3.11]
v = [1.1,2,1,2.15]


value_curr = 0
Max_recorded = -1
w_copy = W
for i in range(len(w)):
	# W=4.11
	W = w_copy
	value_curr = 0
	pivot = w[i]
	if pivot < W:
		W = W - pivot
		value_curr = v[i]
	rem = w[0:i] + w[i+1:]
	Val_rem = v[0:i] + v[i+1:]
	for k in range(len(rem)):
		if rem[k] <= W:
			W -= rem[k]
			value_curr += Val_rem[k]
	Max_recorded = max(Max_recorded, value_curr)

print (Max_recorded)