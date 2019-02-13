#https://practice.geeksforgeeks.org/problems/kth-smallest-element/0/?ref=self
if __name__ =='__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().rstrip().split(" ")))
        k = int(input())-1
        for i in range(1,1001):
            if i in a:
                if k ==0:
                    print(i)
                    break
                k -=1
    