from dts.array import *

### 2.2.1 ###

# (n^3)/1000 - 100(n^2) + 3 ~ O(n^3)

### 2.2.2 (selection sort) ###

def selection_sort(A):
    for i in range(0,A.length() - 1):
        min = i
        for j in range(i + 1,A.length()):
            if A[min] > A[j]:
                min = j
        tmp = A[min]
        A[min] = A[i]
        A[i] = tmp
    return A


# Loop invariant: from 0 to i, array is sorted
# When there is only 2 left element to check, 
# le smallest will be place before se second.
# so the array is sorted

# best case: array already sorted
# O(n^2)

# word case: array sorted in reverse order
# O(n^2)

# best case and word case have the same O 
# because we need to find the smallest value 
# at each iteration, sorted or not.

### 2.2.3 ###

# average case: n/2
# worst case: n

# In both case, n is the biggest term when n -> inf.
# So in both case, the complexity is O(n)

### 2.2.4 ###

# ???



####################################################
### tests ###

A = Array(arr=[9,8,7,6,5,4,3,2,1])

B = selection_sort(A.copy())
A.print()
B.print()

