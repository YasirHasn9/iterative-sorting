def linear_search(arr, target):
    # Your code here
    for i in range(0,len(arr)):
        if target == arr[i]:
            return i
    return -1   # not found

    #    self.assertEqual(linear_search(arr1, 6), -1)
    #     self.assertEqual(linear_search(arr1, -6), 8)
    #     self.assertEqual(linear_search(arr1, 0), 6)
    #     self.assertEqual(linear_search(arr2, 3), -1)
print(linear_search([-2, 7, 3, -9, 5, 1, 0, 4, -6] , -6))

# Write an iterative implementation of Binary Search
def binary_search(arr, target):
    # Your code here
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1

    return -1  # not found


# print(binary_search([-9, -8, -6, -4, -3, -2, 0, 1, 2, 3, 5, 7, 8, 9], -9))
# print(binary_search([0,1], 0))
