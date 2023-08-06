#bubble-sort algorithm, checks if the adjacent element is greater than the current element and swaps if true


test_arr = [55, 22, 35, 45, 15, 19, 18, 28, 1927]


def bubble_sort(arr):
    n = len(arr)

    sorted = False

    while(not sorted):
        sorted = True
        for i in range(n-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
            
    return arr

print(bubble_sort(test_arr))