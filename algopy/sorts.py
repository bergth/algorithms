from array import *

def insertion_sort(A,verbose=False):
	for j in range(1,A.length()):
		if(verbose):
			print(str(j)+": ",end='')
			A.print()
		key = A[j]
		i = j - 1
		while(i>=0 and A[i] > key):
			print(A[i])
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

A = Array(10,arr=[5,2,4,6,1,3])

B = insertion_sort(A.copy(),verbose=True)

