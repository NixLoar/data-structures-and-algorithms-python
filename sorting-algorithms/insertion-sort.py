def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example
arr = [55, 28, 28, 96, 78, 83, 84, 21, 42]
insertion_sort(arr)
print("Insertion Sort:", arr)  