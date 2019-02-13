"""
Given an array A of N positive integers. Find the sum of maximum sum non-decreasing subsequence of the given array.
"""
def max_sum_increase(a):
    n = len(a)
    m = a.copy()
    for i in range(1,n):
        max_sum = 0
        for j in range(i-1,-1,-1):
            if (m[j]>max_sum and a[j] < a[i]):
                max_sum =m[j]
        m[i] += max_sum
    return max(m)

if __name__ =='__main__':
    T = int(input())
    for i in range(T):
        n = int(input())
        a = input().rstrip().split(" ")
        a = [int(a[j]) for j in range(len(a))]
        print(max_sum_increase(a))