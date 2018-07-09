from dts.array import *


def insertion_sort(A,verbose=False):
	for j in range(1,A.length()):
		if(verbose):
			print(str(j)+": ",end='')
			A.print()
		key = A[j]
		i = j - 1
		while(i>=0 and A[i] > key):
			A[i+1] = A[i]
			i = i - 1
		A[i+1] = key
	return A

### 2.1.1

# 31 41 59 26 41 58
# 31 41 59 26 51 58
# 31 45 59 26 41 58
# 26 31 41 59 41 58
# 26 31 41 41 59 58
# 26 31 41 41 58 59

### 2.1.2

def insertion_sort_revert(A,verbose=False):
    for j in reversed(range(0,A.length()-2)):
        if(verbose):
            print(str(j)+": ",end='')
            A.print()
        key = A[j]
        i = j + 1
        while(i < A.length() and A[i] < key):
            A[i-1] = A[i]
            i = i + 1
        A[i-1] = key
    return A

### 2.1.3

def search_in_array(A,v):
	for i in range(0,A.length()):
		if(v == A[i]):
			return i
	return None

# Initialization
# if A.length() == 0, the algorithm will not enter in the for loop
# if A.length() == 1, there is only one element in the array, so it will be test
#						and next the algorithms will return non if A[0] != v
# 
# Maintenance
# if an element is found, the algorithm quit and return i
# else the element is not found and it continue to search
#
# Termination
# The for loop end when i == A.lenght.
# In this case, all the array has been checked. If there is nothing found, the 
# algorithm will return None.

### 2.1.4

# 001010101
#+101000101
#=111011111

def add_binary(A,B):
	if(A.length() != B.length()):
		print("A and B must have the same size")
		return None
	else:
		C = Array(A.length())
		carry = 0
		for i in reversed(range(0,A.length())):
			if((A[i] != 0 and A[i] != 1) or (B[i] != 0 and B[i] != 1)):
				print("Numbers must be binary representation")
				return None
			tmp = A[i] + B[i] + carry
			if(tmp == 0):
				C[i] = 0
				carry = 0
			elif(tmp == 1):
				C[i] = 1
				carry = 0
			elif(tmp == 2):
				C[i] = 0
				carry = 1
			elif(tmp == 3):
				C[i] = 1
				carry = 1
	if(carry == 1):
		print("There is an overflow")
	return C

# tests

A = Array(arr=[31,41,59,26,41,58])

B = insertion_sort_revert(A.copy(),verbose=True)

B.print()

C = Array(arr=[1,5,8,9,5,4,2,3,1,7])

C.print()

print(search_in_array(C,9))
print(search_in_array(C,6))

A = Array(arr=[1,1,1,0,1,0,1,0])
B = Array(arr=[1,0,0,0,0,1,1,1])
A.print()
B.print()
C=add_binary(A,B)
C.print()

