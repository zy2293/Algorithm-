# Algorithm Insertion Sort
# taking running time O(n**2)
def insertSort(A):
    for j in range(1, len(A)):
        key = A[j]
        i = j-1
        while i >=0 and A[i] >key:
            A[i+1] = A[i]
            i = i-1
        A[i+1] = key
    return A

M = [89,34,11,44,22,100,29,15,67,63]
print  (insertSort(M))

# Algorithm MergeSort
# taking running time O(nlogn)

def mergeSort(A):
    lefthalf = []
    righthalf = []
    if len(A) >1: # stop mechanism
        mid = len(A)//2
        lefthalf = A[:mid]
        righthalf = A[mid:]
        mergeSort(lefthalf) # recursion -- divide
        mergeSort(righthalf) # recursion -- divide

# conquer
        i = 0
        j = 0
        k = 0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] <= righthalf[j]:
                A[k] = lefthalf[i]
                i = i+1
            else:
                A[k] = righthalf[j]
                j = j+1
            k = k+1
    return A

print (mergeSort(M))

# Algorithm QuickSort
# taking time worst O(n**2), the best O(nlogn)
def quickSort(A, left, right):
    if left < right:
        split = partition(A, left, right)
        quickSort(A, left, split-1)
        quickSort(A, split+1, right)

    return A
def partition(A, left, right):
    pivot = A[right]
    split = left -1
    for j in range(left, right):
        if A[j] <= pivot:
            temp = A[j]
            A[j] = A[split+1]
            A[split+1] = temp
            split = split+1

    A[right] = A[split+1]
    A[split+1] = pivot
    return split+1
print  (quickSort(M, 0, len(M)-1))
