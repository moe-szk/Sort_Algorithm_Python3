# Function : Bubble Sort 
def bubble_sort(A_array):
    # Find the minimal value's location in unsorted array
    for i in range(len(A_array)):
        min_index = i 
        for j  in range(1,len(A_array)-1):
            if A_array[j] > A_array[j+1]:
            # Swap A[j] with A[j+1]
                A_array[j], A_array[j+1] = A_array[j+1],A_array[j]
    return A_array