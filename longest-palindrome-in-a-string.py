def check_palidrome(s):
    return s[::-1] == s 
if __name__=='__main__':
    t = int(input())
    for _ in range(t):
        s = input()
        maxS = 0 
        re = ""
        for i in range(len(s)):
            for j in range(i+1, len(s)+1):
                if (len(s[i:j]) > maxS and check_palidrome(s[i:j])):
                    re = s[i:j]
                    maxS = len(s[i:j])
        print(re)