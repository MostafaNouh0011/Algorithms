
def Heapify(array, n, i):
    l = 2*i + 1
    r = 2*i + 2
    maximum = i

    if l < n and array[l] > array[maximum]:
        maximum = l

    if r < n and array[r] > array[maximum]:
        maximum = r

    if maximum != i:
        array[i], array[maximum] = array[maximum], array[i]
        Heapify(array, n, maximum)


def Build_Heap(array, n):
    for i in range(n//2-1, -1, -1):
        Heapify(array, n, i)

def Heap_Sort(array):
    n = len(array)

    Build_Heap(array, n)

    for i in range(n-1, 0, -1):
        array[0], array[i] = array[i], array[0]
        Heapify(array, i, 0)


if __name__ == "__main__":
    arr = [2, 5, 4, 6, 1, 3]
    Heap_Sort(arr)
    print(arr)