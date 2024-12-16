import math

def jump_search(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    prev = 0

    while prev < n and arr[min(step, n) - 1] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return -1

    for i in range(prev, min(step, n)):
        if arr[i] == target:
            return i

    return -1

# Example

array = [55, 28, 28, 96, 78, 83, 84, 21, 42]
array.sort()
target = 96

jump_result = jump_search(array, target)
print(f"Jump Search: {target} found at index {jump_result}" if jump_result != -1 else "Jump Search: Target not found")