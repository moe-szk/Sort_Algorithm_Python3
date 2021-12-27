# import sorting algorithm
from selection_sort import selection_sort
from bubble_sort import bubble_sort
from heap_sort import heap_sort
from merge_sort import merge_sort
from quick_sort import quick_sort

#from numpy import random
from isSorted import isSorted
import numpy as np
from time import process_time

# Input the number of data.
print("Input the number of data.")
n = input()

# Generate array of random numbers
A = np.random.randint(int(n),size=int(n))

# Sort
m = int(1)
while int(m) != 0:
    print("1:Selection Sort\n2:Bubble Sort\n3:Heap Sort\n4:Merge Sort\
    \n5:Quick Sort\n0:Quit")
    
    m = input()

    t1 = process_time()
    if int(m)==1:   
        sorted_A = selection_sort(A)
    elif int(m)==2:
        sorted_A = bubble_sort(A)
    elif int(m)==3:
        sorted_A = heap_sort(A)
    elif int(m)==4:
        sorted_A = merge_sort(A)
        print(sorted_A)
    elif int(m)==5:
        sorted_A = quick_sort(A)
    t2 = process_time()
    
# Check and output
    print("isSorted",isSorted(n,sorted_A))
    print("Time : ",(t2-t1))
    