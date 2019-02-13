import math 
def max_sum(array):
    n = len(array)
    curMax = array[0]
    resMax = array[0]
    for i in range(n-1):
        curMax = max(array[i+1],array[i+1]+curMax)
        resMax = max(resMax,curMax)
    return resMax 

if __name__=='__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = input()
        arr = arr.rstrip().split(' ')
        arr = [int(arr[j]) for j in range(len(arr))]
        print(max_sum(arr))
