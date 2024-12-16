def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1

# Example

array = [17, 25, 16, 80, 79]
target = 25

linear_result = linear_search(array, target)
print(f"Linear Search: {target} found at index {linear_result}" if linear_result != -1 else "Linear Search: Target not found")