from random import random


def fillArr(arr, n):
    for i in range(0, n):
        arr.append(int(random() * 100))
    return arr


def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)


def heapSort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

if __name__ == '__main__':
    n = 10
    arr = []

    fillArr(arr, n)
    print("Unsorted array is")
    for i in range(len(arr)):
        print(arr[i], end=" ")

    heapSort(arr)
    print("\nSorted array is")
    for i in range(len(arr)):
        print(arr[i], end=" ")