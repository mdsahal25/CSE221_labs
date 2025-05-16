def merge(left, right):
    merged = []
    inv_count = 0
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
            inv_count += len(left) - i
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged, inv_count
def merge_sort_with_inversions(arr):
    if len(arr) <= 1:
        return arr, 0
    mid = len(arr) // 2
    left, inv_left = merge_sort_with_inversions(arr[:mid])
    right, inv_right = merge_sort_with_inversions(arr[mid:])
    merged, split_inv = merge(left, right)
    total_inv = inv_left + inv_right + split_inv
    return merged, total_inv
n = int(input())
arr = list(map(int, input().split()))
sorted_arr, inversions = merge_sort_with_inversions(arr)
print(inversions)
print(*sorted_arr, end=" ")