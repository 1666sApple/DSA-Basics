import array

arr = array.array('i', [6, 1, 7, 4, 2, 9, 8, 5, 3])

def insertion_sort(arr):
    size = len(arr)

    for i in range(1, size):
        temp = arr[i]
        j = i - 1
        while j>=0 and arr[j] > temp:
            arr[j+1] = arr[j]
            j -= 1
        
        arr[j+1] = temp
    
    return arr

sort_arr = insertion_sort(arr)

print(sort_arr)