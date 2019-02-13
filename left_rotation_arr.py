import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def rotLeft(a, d):
    n = len(a)
    temp_a = [0 for _ in range(n)]
    for i in range(n):
        new_i = (i-d+n)%n
        temp_a[new_i] = a[i]
    return temp_a 

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nd = raw_input().split()

    n = int(nd[0])

    d = int(nd[1])

    a = map(int, raw_input().rstrip().split())

    result = rotLeft(a, d)

    print result
    # fptr.write(' '.join(map(str, result)))
    # fptr.write('\n')

    # fptr.close()
