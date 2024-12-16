def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Example
arr = [75, 85, 84, 85, 9, 60, 2, 12]
selection_sort(arr)
print("Selection Sort:", arr) 