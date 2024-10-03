import array

arr = array.array('i', [12, 25, 11, 34, 90, 22])

def bubble_sort(arr):
    size = len(arr)
    for j in range(size):
        for i in range(0, size-1-j):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]

    return arr

sort_arr = bubble_sort(arr)
print(sort_arr)