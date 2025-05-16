def OBT(sorted_array, start, end, result):
    if start > end:
        return
    middle = (start + end) // 2
    result.append(sorted_array[middle])
    OBT(sorted_array, start, middle - 1, result)
    OBT(sorted_array, middle + 1, end, result)
    return result
num_elements = int(input())
values = list(map(int, input().split()))
output = []
tree_order = OBT(values, 0, len(values) - 1, output)
print(*tree_order[:num_elements])