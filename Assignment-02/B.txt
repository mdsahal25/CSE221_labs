def partition(arr3,start,end):
    middle = arr3[end]
    i = start -1
    for j in range(start,end):
        if arr3[j]<middle:
            i+=1
            temp = arr3[i]
            arr3[i] = arr3[j]
            arr3[j] = temp
    i+=1
    temp = arr3[i]
    arr3[i] = arr3[end]
    arr3[end] = temp
    return i
def quicksrt(arr3,start,end):
    if end<= start:
        return
    middle = partition(arr3,start,end)
    quicksrt(arr3,start,middle-1)
    quicksrt(arr3,middle+1,end)
n1 = int(input())
arr1 = list(map(int,input().split()))
n2 = int(input())
arr2 = list(map(int,input().split()))
arr3 = arr1+arr2
temp = []
start = 0 
end = len(arr3)-1
quicksrt(arr3,start,end)
for i in arr3:
    print(i,end=' ')