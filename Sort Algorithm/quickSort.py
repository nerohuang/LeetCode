nums = [3,2,3,1,2,4,5,5,6]

def partition(arr, left, right):
    pivot = left
    j = left + 1
    for i in range(left + 1, right + 1):
        if arr[i] > arr[pivot]:
            arr[j], arr[i] = arr[i], arr[j]
            j += 1;
    arr[pivot], arr[j - 1] = arr[j - 1], arr[pivot]
    return j - 1

def quickSort(arr, left = 0, right = len(nums) - 1):
    if left < right:
        pivot = partition(arr, left, right);
        quickSort(arr, left, pivot - 1);
        quickSort(arr, pivot + 1, right)

quickSort(nums)
