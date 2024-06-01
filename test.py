list = [ 12, 8, 9, 3, 11, 5, 4]
"""
mid = len(list)//2
left_array = list[0: mid]
print(left_array)
right_array = list[mid:len(list)]
print(right_array)
"""
def mergesort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_array = arr[:mid]
        #print(left_array)
        right_array = arr[mid:]
        #print(right_array)
        mergesort(left_array)
        mergesort(right_array)
        #print(left_array)
        #print(right_array)
        i = 0 #index of left array
        j = 0 #index of right array
        k = 0 #index of arr
        # Merge the two sorted halves
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                arr[k] = left_array[i]
                i += 1
            else:
                arr[k] = right_array[j]
                j += 1
            k += 1
        # Check for any remaining elements in the left half
        while i < len(left_array):
            arr[k] = left_array[i]
            i += 1
            k += 1
        # Check for any remaining elements in the right half
        while j < len(right_array):
            arr[k] = right_array[j]
            j += 1
            k += 1

    
mergesort(list)
print(list)