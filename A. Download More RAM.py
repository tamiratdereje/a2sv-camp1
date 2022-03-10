import heapq
t = int(input())

for i in range(t):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    visited = set()
    li = []
    for i in range(n):
        heapq.heappush(li, (a[i], b[i]))
    for j in range(n):
        tempCapa, capaIncr = heapq.heappop(li)
        if tempCapa <= k:
            k+=capaIncr
    print(k)
