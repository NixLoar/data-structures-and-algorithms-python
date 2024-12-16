def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

# Example
arr = [80, 18, 36, 38, 52, 56, 40, 51, 59]
sorted_arr = quick_sort(arr)
print("Quick Sort:", sorted_arr) 