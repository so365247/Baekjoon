n, l = map(int, input().split())        # l = 길이, n = 과일 개수, h = 먹을 과일 크기
h = list(map(int, input().split()))

h.sort()

for i in h:
    if i <= l:
        l += 1
    else:
        break

print(l)