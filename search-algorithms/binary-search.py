def binary_search(arr, target):
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = left + (right - left) // 2  # Avoids overflow

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

# Example

array = [1, 3, 5, 7, 9, 11, 13, 15]
target = 7

binary_result = binary_search(array, target)
print(f"Binary Search: {target} found at index {binary_result}" if binary_result != -1 else "Binary Search: Target not found")
