A = [2,4,15,17,19,21,25,32,34]
B = [6,8,10,11,13,23,27,30,36]
C = [1,5,9,14,16,20,24,31,33]
D = [3,7,12,18,22,26,28,29,35]
allCombs = [A,B,C,D]
counter = 0

hasAny = [1,1,1,1]

n1 = int(input())
n2 = int(input())
n3 = int(input())
n4 = int(input())
n5 = int(input())
n6 = int(input())
n7 = int(input())
n8 = int(input())

ep = [n1,n2,n3,n4,n5,n6,n7,n8]

while 1:
	a = input()
	ep.append(int(a))
	for i in range(0,4):
		hasAny[i] = 1
	for each in ep[-9:]:
		if each in A:
			hasAny[0] = 0
		elif each in B:
			hasAny[1] = 0
		elif each in C:
			hasAny[2] = 0
		elif each in D:
			hasAny[3] = 0
	for i in range (0,4):
		if hasAny[i] == 1:
			print(allCombs[i])
	if 1 not in hasAny:
		print("skip bate")
	counter += 1

