import array 

arr = array.array('i', [12, 11, 13, 5, 7, 6])

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    sub_arr1 = arr[:mid]
    sub_arr2 = arr[mid:]

    sub_arr1 = merge_sort(sub_arr1)
    sub_arr2 = merge_sort(sub_arr2)

    return merge(sub_arr1, sub_arr2)

def merge(left, right):
    new = []
    i, j = 0, 0

    while i < len(left) and j < len(right):
        if left[i]<right[j]:
            new.append(left[i])
            i+=1
        else:
            new.append(right[j])
            j+=1

    
    new.extend(left[i:])
    new.extend(right[j:])

    return new

sort_array = merge_sort(arr)
print(sort_array)