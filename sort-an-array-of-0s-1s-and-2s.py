"""
Given an array A of size N containing 0s, 1s, and 2s; you need to sort the array in ascending order.
"""
if __name__ == '__main__':
    
    T = int(input())
    for i in range(T):
        s = {0:0,1:0,2:0}
        n = int(input())
        a = input().rstrip().split(' ')
        a = [int(a[j]) for j in range(len(a))]
        for j in range(len(a)):
            s[a[j]] +=1
        re = ""
        for j in range(3):
            c = s[j]
            if c>0:      
                for k in range(c):
                    re = re + str(j) + " "
        print(re)
        