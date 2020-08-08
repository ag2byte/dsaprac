# t = int(input())
def getlist():
    x, y = map(int, input().split())
    ar1 = list(map(int, input().split()))
    ar2 = list(map(int, input().split()))
    i = j = 0
    l = []
    while i < x and j < y:
        if ar1[i] <= ar2[j]:
            l.append(ar1[i])
            i += 1
        else:
            l.append(ar2[j])
            j += 1

    for p in range(i, x):
        l.append(ar1[i])
        i += 1
    for p in range(j, y):
        l.append(ar2[j])
        j += 1
    return l


for _ in range(int(input())):
    l = getlist()
    for i in l:
        print(i, end=" ")
    print("")
