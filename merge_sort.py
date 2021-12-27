# Function : Merge Sort 
def merge_sort(A_array):

    if len(A_array) > 1:

        middle_index = len(A_array)//2 

        Left_array  = A_array[:middle_index]
        Right_array = A_array[middle_index:]
        
        merge_sort(Left_array)
        merge_sort(Right_array)

        i = j = k = 0

        while int(i) < len(Left_array) and int(j) < len(Right_array):
            if Left_array[i] < Right_array[j]:
                A_array[k] = Left_array[i]
                i += 1
            else:
                A_array[k] = Right_array[j]
                j += 1
            k += 1
        
        while int(i) < len(Left_array):
            A_array[k] = Left_array[i]
            i += 1
            k += 1
        
        while int(j) < len(Right_array):
            A_array[k] = Right_array[j]
            j += 1
            k += 1

    return A_array