print("Hello World!")

def binary_search(list, item):
    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2
        guess = list[mid]

        if guess == item:
            return mid
        if guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i

    return smallest_index

def selectionSort(arr):
    newArr = []

    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))

    return newArr

my_list = [1, 3, 5, 7, 9]

print(selectionSort([5, 3, 6, 2, 10]))
print(binary_search(my_list, 3))
print(binary_search(my_list, -1))
