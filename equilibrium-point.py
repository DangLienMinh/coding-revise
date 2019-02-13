"""
Given an array A of N positive numbers. The task is to find the position where equilibrium first occurs in the array.
Equilibrium position in an array is a position such that the sum of elements below it is equal to the sum of elements after it.
"""
if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = input().rstrip().split()
        a = [int(a[j]) for j in range(len(a))]
        if len(a) ==1:
            print(1)
        elif (len(a) == 2):
            print(-1)
        else:
            sumCheck = sum(a)
            re = -1 
            sumStart = a[0]
            c = 1
            while(c < len(a)):
                if (sumCheck - a[c] - sumStart == sumStart):
                    re = c+1
                    break
                sumStart += a[c]
                c +=1
                
            print(re)