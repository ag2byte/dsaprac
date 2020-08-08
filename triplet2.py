def counttriplet(ar, n):
    ar.sort()
    # i = 0
    s = n-1
    # j = s-2
    c = 0
    while s >= 0:
        i = 0
    # s = n-1
        j = s-1
        while i < j:
            if ar[s] == ar[i]+ar[j]:
                c += 1
                print(ar[i], ar[j], ar[s])
                break
            elif ar[s] > ar[i]+ar[j]:
                i += 1
            else:
                j -= 1

        s = j

    if c > 0:
        return c
    else:
        return -1


ans = []
for i in range(0, int(input())):
    n = int(input())
    ar = list(map(int, input().split()))
    ans.append(counttriplet(ar, n))

for i in ans:
    print(i)
