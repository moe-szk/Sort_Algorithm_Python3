# Function : Heap Sort 

# Heapify function
def heapify(A_array,n,i):
    # Find largest among root, left child and right child.
    largest = i 
    left    = 2 * i + 1
    right   = 2 * i + 2 

    if left < n and A_array[left] > A_array[largest]:
        largest = left 
    
    if right < n and A_array[right] > A_array[largest] :
        largest = right
    
    # Swap and continue heapifying if root isn't largest
    if largest != i :
        A_array[i] , A_array[largest] = A_array[largest] , A_array[i]
        heapify(A_array,n,largest)

# The main function 
def heap_sort(A_array):
    n = len(A_array)

    for i in range(n//2,-1,-1):
        heapify(A_array,n,i)

    for i in range(n-1,0,-1):
        A_array[i], A_array[0] = A_array[0], A_array[i]
        heapify(A_array,i,0)
    return A_array