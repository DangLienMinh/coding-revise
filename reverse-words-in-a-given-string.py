if __name__ =='__main__':
    T = int(input())
    for i in range(T):
       s = input().rstrip().split(".")
       re = ".".join(s[::-1])
       print(re)