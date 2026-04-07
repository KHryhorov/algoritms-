def bin_search(arr:list,key: int)->bool:
    """
    This function is used to find the index of an element in a sorted array (with binary search algorithm)

    :param arr: your sorted array
    :return: True if item found or False if not
    """
    L=0
    R=len(arr)-1
    while L<=R:
        mid = (L + R) // 2
        if key == arr[mid]:
            return True
        if key < arr[mid]:
            R= mid -1
        else:
            L = mid + 1
    if arr[L] == key:
        return True
    else:
        return False

array=[1,3,5,6,7,9,23,34,54,67,78,98,111,333,555,666,777,888,999,1000]
print(bin_search(array,5))