
def quick_sort(lst):
    if len(lst) < 2:
        return lst
    else:
        pivot = lst[0]
        less = [i for i in lst[1:] if i <= pivot]
        greater = [j for j in lst[1:] if j > pivot]
        
        return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([2, 5, 4, 6, 1, 3]))
####################################################################

def partition(lst, start, end):
    piv, ptr = lst[end], start

    for i in range(start, end):
        if lst[i] <= piv:
            lst[i], lst[ptr] = lst[ptr], lst[i]
            ptr += 1
    
    lst[end], lst[ptr] = lst[ptr], lst[end]
    return ptr

def QuickSort(lst, start, end):
    if len(lst) == 1:
        return lst
    if start < end:
        pivot = partition(lst, start, end)
        QuickSort(lst, start, pivot-1)
        QuickSort(lst, pivot+1, end)
    return lst

if __name__ == "__main__":
    lst = [2, 5, 4, 6, 1, 3]

    QuickSort(lst, 0, len(lst)-1)
    print(lst)

