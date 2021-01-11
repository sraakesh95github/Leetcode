def binary_search_inner(lst, start, end, ele):
    i = int((start + end) / 2)
    print(lst[i])
    print("Element: " + str(ele))
    if (lst[i] == ele):
        print("Entered found case..." + str(i))
        return i
    #         print(i)
    #         return i
    else:
        if (lst[i] < ele):
            if (start <= end):
                start = i + 1
                binary_search_inner(lst, start, end, ele)
            else:
                return -1
        else:
            if (start <= end):
                end = i - 1
                print("End: " + str(end))
                binary_search_inner(lst, start, end, ele)
            else:
                return -1


def binary_search(lst, ele):
    print(binary_search_inner(lst, 0, len(lst) - 1, ele))


if __name__ == "__main__":
    lst = [4, 6, 7, 9, 10, 23, 45, 67]
    # print(binary_search(lst, 6))
    binary_search(lst, 6)