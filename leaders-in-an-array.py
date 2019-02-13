"""
Given an array of positive integers. Your task is to find the leaders in the array.
Note: An element of array is leader if it is greater than or equal to all the elements to its right side. 
Also, the rightmost element is always a leader. 
"""
def leader_arr(arr):
    res = str(arr[len(arr)-1])
    maxVal = arr[len(arr)-1]
    for i in range(len(arr)-2,-1,-1):
        if arr[i] >=maxVal:
            maxVal = arr[i]
            res = str(arr[i]) +" "+res 
    return res
if __name__ =='__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = input().rstrip().split(" ")
        a = [int(a[i]) for i in range(len(a))]
        print(leader_arr(a))