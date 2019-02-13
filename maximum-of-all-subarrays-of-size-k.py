if __name__ =='__main__':
    n=int(input())
    for _ in range(n):
        m,k=input().split()
        m=int(m)
        k=int(k)
        l=list(map(int,input().split()))
        s=[]
        for i in range(0,len(l)-k+1):
            s.append(max(l[i:i+k]))
        print(' '.join([str(i) for i in s]))