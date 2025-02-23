def make(n):
    l = []
    for i in range(n):
        x = int(input("Enter the values: "))
        l.append(x)
    return l

def find(arr, target):
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i]+arr[j]==target:
                return [i, j]
    return []

a= make(4)
find(a, 9)
