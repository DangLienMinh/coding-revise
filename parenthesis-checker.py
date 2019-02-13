"""
Parenthesis Checker
"""
def check_balanced_parenthese(s):
    c = 0 
    if (s[0]=='}' or s[0]==")" or s[0]=="]"):
        print("not balanced")
    for i in range(len(s)):
        if s[i] == "{":
            c +=1
        elif s[i] =="(":
            c +=2 
        elif s[i] =="[":
            c +=3
        elif s[i] =="]":
            c -=3 
        elif s[i] ==")":
            c -=2
        elif s[i] == "}":
            c -=1
    if c ==0:
        print("balanced")
    else:
        print("not balanced")

if __name__ =='__main__':
    t = int(input())
    for i in range(t):
        s = input().rstrip()
        check_balanced_parenthese(s)
        