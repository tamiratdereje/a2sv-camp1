t = int(input())
for i in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    arr.sort()
    
    sumR = arr[-1]
    sumB = arr[0] + arr[1]
    countB = 1
    countR = len(arr)-1
    
    while countB < countR:
        if sumB < sumR:
            print("YES")
            break
        
        countR-=1
        countB+=1
        sumB+=arr[countB]
        sumR+=arr[countR]
        if countB >= countR:
             print("No")
             break
        
