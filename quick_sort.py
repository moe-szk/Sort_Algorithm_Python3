# Function : Quick Sort 
def quick_sort(A_array):
    n = len(A_array)

    if n < 2 :
        return
    
    pivot_index = 0

    # Partition
    for i in range(1,n):
        if A_array[i] <= A_array[0]:
            pivot_index += 1
            A_array[i],A_array[pivot_index] = A_array[pivot_index], A_array[i]
    
    A_array[0],A_array[pivot_index] = A_array[pivot_index],A_array[0]

    # Separately sort
    Left_array  = quick_sort(A_array[0:pivot_index])
    Right_array = quick_sort(A_array[pivot_index+1:n])

    return A_array 