def getMax(ar, n):
    m = 0
    for i in range(0, n):
        for j in range(i+1, n):
            if ar[i] <= ar[j] and j-i > m:
                m = j-i
            else:
                continue
    return m


for _ in range(0, int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    print(getMax(ar, n))
