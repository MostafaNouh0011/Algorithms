
def bubble_sort(lst):
    flag = True
    for i in range(len(lst)-1):
        for j in range(len(lst)-1 - i):
            if lst[j] > lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
                flag = False

        if flag == True:
            break

    return lst


if __name__ == "__main__":
    lst = [2, 5, 4, 6, 1, 3]
    bubble_sort(lst)
    print(lst)
