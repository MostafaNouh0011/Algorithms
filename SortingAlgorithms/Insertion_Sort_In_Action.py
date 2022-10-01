
def insertionSort1(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j+1] = arr[j]
            j -= 1
            print(*arr)
        arr[j+1] = key
    print(*arr)

if __name__ == '__main__':
    arr = [2, 5, 4, 6, 1, 3]
    insertionSort1(arr) 