def Rearrange(ar, n):
    i = 0
    j = n-1
    k = 1
    while i <= j:
        if k % 2 == 0:
            print(ar[i], end=" ")
            i += 1
        else:
            print(ar[j], end=" ")
            j -= 1
        k += 1


for _ in range(int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    Rearrange(ar, n)
    print("")
