# # t = int(input())
# # while t != 0:

def subarray(ar, n, s):

    # n, s = map(int, input().split())
    # ar = list(map(int, input().split()))
    found = False
    sum = l = i = 0
    for i in range(0, n+1):
        sum += ar[i]
        if sum > s:
            sum -= ar[l]
            l += 1
        if sum == s:
            found = True
            break
    # print(sum)
    return found, i, l


f_list = []
t = int(input())
for p in range(0, t):
    n, s = map(int, input().split())
    ar = list(map(int, input().split()))
    found, i, l = subarray(ar, n, s)
    if found:
        f_list.append([l+1, i+1])
    else:
        f_list.append([-1])

for p in range(0, t):
    for i in f_list[p]:
        print(i, end=" ")
    print("")
