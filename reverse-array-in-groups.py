if __name__ =='__main__':
    t = int(input())
    for _ in range(t):
        n,k = input().rstrip().split(" ")
        n = int(n)
        k = int(k)
        a = list(map(int,input().rstrip().split(" ")))
        c = 0
        temp =[]
        s ="" 
        for i in range(len(a)):
            temp.append(a[i])
            if (c == k-1):
                s =s +' '.join([str(temp[k]) for k in range(len(temp)-1,-1,-1)]) + ' '
                temp =[] 
                c = 0 
            else:
                c +=1
        s =s+' '.join([str(temp[k]) for k in range(len(temp)-1,-1,-1)])
        print(s)