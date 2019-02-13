"""
How to Find all Pairs in Array of Integers Whose sum is Equal to a Given Number
"""
def find_pairs(arr,check):
    temp = []
    for i in range(len(arr)):
        t = check - arr[i]
        if t not in temp:
            temp.append(arr[i])
        else:
            temp.append(arr[i])
            print("{} {}\n".format(t,arr[i]))

if __name__ =='__main__':
    t = int(input())
    for i in range(t):
        s = int(input())
        arr = input().rstrip().split(" ")
        arr = [int(arr[i]) for i in range(len(arr))]
        find_pairs(arr,s)
