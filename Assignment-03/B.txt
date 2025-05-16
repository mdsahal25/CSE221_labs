def max_pair(arr, left, right):
    if right - left < 1:
        return float('-inf')
    if right - left == 1:
        return arr[left] + arr[right]**2
    mid = (left + right) // 2
    left_max = max_pair(arr, left, mid)
    right_max = max_pair(arr, mid, right)
    
    max_squared_right = float('-inf')
    for j in range(mid, right + 1):
        max_squared_right = max(max_squared_right, arr[j]**2)
    cross_max = float('-inf')
    for i in range(left, mid):
        cross_max = max(cross_max, arr[i] + max_squared_right)
    return max(left_max, right_max, cross_max)
n = int(input())
arr = list(map(int, input().split()))
result = max_pair(arr, 0, n-1)
print(result)