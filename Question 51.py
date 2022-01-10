def binary_search(list,key):
    list.sort()
    max = len(list) - 1
    min = 0
    while max > min:
        mid = (max + min) // 2
        if list[mid] == key:
            return mid
        elif list[mid] > key:
            max = mid - 1
        elif list[mid] < key:
            min = mid + 1
        else:
            return mid
    return -1

list = [1,2,3,9,11,5,4,7]
key = 7
list.sort()
print(list)
result = binary_search(list,key)
if result == -1:
    print("Key is not available.")
else:
    print("key is at: " + str(result))
            