def Unique(x):
    test = [False for _ in range(256)]
    for i in range(len(x)):
        c = ord(x[i])
        if (test[c] == True):
            return False
        else:
            test[c] = True
    return True 

def is_permutation(a,b):
    if len(a) != len(b):
        return False 
    count = [0 for _ in range(256)]
    for s in a:
        c = ord(s)
        count[c] +=1 
    for s in b:
        c = ord(s)
        count[c] -=1 
        if (count[c]<0):
            return False 
    return True

def set_row_column_zero(m):
    m,n  = m.shape

def is_subString(s1,s2):
    return s1.find(s2) !=-1

def is_rotation(s1,s2):
    return is_subString(s1+s1,s2)

def compress_string(s):
    count = 1 
    i =0 
    temp = ''
    last = s[0]
    for i in range(1,len(s)):
        if (s[i] == last):
            count +=1 
        else:
            temp = temp + last + str(count)
            last = s[i]
            count = 1
    
    temp = temp + last + str(count)
    if len(temp)>=len(s):
        return s
    else:
        return temp


if __name__ =='__main__':
    a = raw_input()
    b = raw_input()
    print is_rotation(a,b)

    
    