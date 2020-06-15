import random
size = 10
my_range = 100

my_random = random.sample(range(my_range), size)
print(my_random)
searching_for = 7


def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return True

    return False


print(linear_search(my_random), searching_for))

