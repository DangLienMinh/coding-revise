"""
Given an unsorted array A of size N of non-negative integers, 
find a continuous sub-array which adds to a given number.
"""
def sub_sum(array, check_sum):
    startIdx = 0 
    endIdx = 0 
    counter = 0
    s = 0 
    arr_size = len(array)
    while(counter < arr_size):
        s += array[counter]
        endIdx = counter 
        while (s > check_sum):
            s -= array[startIdx]
            startIdx +=1
        if (s == check_sum):
            break
        counter +=1
    return startIdx, endIdx, s 

if __name__ =='__main__':
    T = int(input())
    for i in range(T):
        l = input().rstrip().split(' ')
        n,s = int(l[0]),int(l[1])
        arr = input().rstrip().split(' ')
        arr = [int(arr[j]) for j in range(len(arr))]
        startIdx, endIdx, r = sub_sum(arr,s)
        if (r==s):
            print("{} {}".format(startIdx+1, endIdx+1))
        else:
            print("-1")
