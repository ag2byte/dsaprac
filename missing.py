def ret_missing(ar, n):
    i = 0
    j = n-1
    while i < j and ar[i+1] == ar[i]+1 and ar[j-1] == ar[j]-1:
        i += 1
        j -= 1
    if ar[i+1] != ar[i]+1:
        return ar[i]+1
    elif ar[j-1] != ar[j]-1:
        return ar[j]-1


t = int(input())
for _ in range(0, t):
    n = int(input())
    ar = list(map(int, input().split()))
    print(ret_missing(ar, len(ar)))
