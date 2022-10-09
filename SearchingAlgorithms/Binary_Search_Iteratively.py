def binary_search_iter(arr, key):

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if key == arr[mid]:
            return mid
        elif key < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    
    return None

if __name__ == "__main__":
    arr = [2, 4, 5, 8, 12, 15]
    print(binary_search_iter(arr, 12))
