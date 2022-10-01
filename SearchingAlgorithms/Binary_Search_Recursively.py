
def binary_search_rec(lst, key, left, right):

    if left <= right:
        mid = (left + right) // 2
    
        if lst[mid] == key:
            return mid
        elif lst[mid] > key:
            return binary_search_rec(lst, key, left, mid - 1)
        else:
            return binary_search_rec(lst, key, mid + 1, right)

    return None


if __name__ == "__main__":
    lst = [2, 4, 5, 8, 12, 15]

    print(binary_search_rec(lst, 8, 0, len(lst)-1))