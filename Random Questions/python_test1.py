#find the rank problem from goldman sachs
n = 2
performance = [[79,89,15],[85,89,82],[71,96,88]]
x = []

for i in range(len(performance)):

	# print (sum(i))
	x.append([i,sum(performance[i])])
print(x)
x.sort(key=lambda x: x[1])
print (x[n])

