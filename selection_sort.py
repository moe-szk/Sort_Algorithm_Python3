# Function : Selection Sort 
def selection_sort(A_array):
    # Find the minimal value's location in unsorted array
    for i in range(len(A_array)):
        min_index = i 
        for j  in range(i+1,len(A_array)):
            if A_array[min_index] > A_array[j]:
                min_index = j 
        # Swap A[i] with A[min_index]
        A_array[i], A_array[min_index] = A_array[min_index],A_array[i]
    return A_array