import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    s = [0 for _ in range(256)]
    for c in a:
        idx = ord(c)
        s[idx] +=1
    count = 0
    for c in b:
        idx = ord(c)
        s[idx] -=1
    for i in range(256):
        count += abs(s[i])
    return count



if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = raw_input()

    b = raw_input()

    res = makeAnagram(a, b)
    print res

    # fptr.write(str(res) + '\n')

    # fptr.close()