def isSorted(n,A_array):
    test_flag = True
    for i in range(1,len(A_array)):
        if(A_array[i]<A_array[i-1]):
            test_flag = False
    if int(n) != len(A_array):
        test_flag = False
    return test_flag
