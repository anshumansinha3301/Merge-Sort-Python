count = 0

def merge_sort(array):
    if len(array) == 1:
        return array
    else:
        mid = len(array)//2
        left_array = array[:mid]
        right_array = array[mid:]
        print(f'Left : {left_array}')
        print(f'Right : {right_array}')
        return merge(merge_sort(left_array),merge_sort(right_array))


def merge(left, right):
    l = len(left)
    r = len(right)
    left_index = 0
    right_index = 0
    sorted_array = [] #code by Anshuman 
    while (left_index < l and right_index < r):
        global count
        count += 1
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    print(sorted_array + left[left_index:] + right[right_index:])
    return sorted_array + left[left_index:] + right[right_index:]



array = [5,9,3,10,45,2,0]
print(merge_sort(array))
print(f'Number of comparisons = {count}')


sorted_array = [5,6,7,8,9]
print(merge_sort(sorted_array))
print(f'Number of comparisons = {count}')

reverse_sorted_array = [9,8,7,6,5,4,3,2,1,0,-1,-2,-3,-4,-5,-6,-7,-8,-9,-10]
print(merge_sort(reverse_sorted_array))
print(f'Number of comparisons = {count}')
