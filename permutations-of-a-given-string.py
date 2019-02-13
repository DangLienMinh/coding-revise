all_permute = set()
def swap(s,i,j):
    list_char = [s[i] for i in range(len(s))]
    temp = list_char[i]
    list_char[i] = list_char[j]
    list_char[j] = temp 
    return "".join(list_char) 
def permute(s, l, r):
    if (l==r):
        all_permute.add(s)
    else:
        for i in range(l,r+1,1):
            s= swap(s,l,i)
            permute(s,l+1,r)
            s = swap(s,l,i)

if __name__ =='__main__':
    T = int(input())
    for i in range(T):
        s = input()
        permute(s,0, len(s)-1)
        all_permute=sorted(all_permute,key = lambda s : s.lower())
        print(" ".join(all_permute))
        all_permute = {}
