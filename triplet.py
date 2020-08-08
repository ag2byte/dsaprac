
def count(ar, n):
    c = 0
    ar.sort()
    m = ar[-1]  # max value
    for i in range(0, n):
        for j in range(i+1, n):
            sum = ar[i] + ar[j]
            if sum > max:
                # not possible
                break
            elif sum in ar:
                c += 1
    if c > 0:
        return -1
    else:
        return c


t = int(input())
l = []
for i in range(0, t):
    n = int(input())
    ar = list(map(int, input().split()))
    c = count(ar, n)
    l.append(c)

for i in range(0, t):
    print(l[i])
