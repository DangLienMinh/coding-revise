def missing_num(arr,n):
    expect = n*(n+1)//2
    t = 0 
    for i in range(len(arr)):
        t += arr[i]
    return expect - t

if __name__=='__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        arr = input()
        arr = arr.rstrip().split(' ')
        arr = [int(arr[j]) for j in range(len(arr))]
        print(missing_num(arr,n))