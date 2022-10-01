# This is merge sort algorithm, It is useful for sorting linked list in O(n log n) time

def Merge(lst, start, mid, end):

    left = lst[:mid]   # Left half
    right = lst[mid:]  # Right half

    k = i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            lst[k] = left[i]
            i +=1
        else:
            lst[k] = right[j]
            j += 1
        k += 1

    while i < len(left):
        lst[k] = left[i]
        i += 1
        k += 1
    
    while j < len(right):
        lst[k] = right[j]
        j += 1
        k += 1

def MergeSort(lst, start, end):
    if start < end:
        mid = (start + (end-1)) // 2
        MergeSort(lst, start, mid)
        MergeSort(lst, mid+1, end)
        Merge(lst, start, mid, end)


if __name__ == "__main__":
    lst = [2, 5, 4, 6, 1, 3]
    MergeSort(lst, 0, len(lst)-1)
    print(lst)