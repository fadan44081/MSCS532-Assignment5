import random
import time

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quicksort(arr, low, pi - 1)
        quicksort(arr, pi + 1, high)


def randomized_partition(arr, low, high):
    random_index = random.randint(low, high)
    arr[random_index], arr[high] = arr[high], arr[random_index]
    return partition(arr, low, high)


def randomized_quicksort(arr, low, high):
    if low < high:
        pi = randomized_partition(arr, low, high)
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)


def generate_random_array(size):
    return [random.randint(1, 10000) for _ in range(size)]


def generate_sorted_array(size):
    return list(range(size))


def generate_reverse_sorted_array(size):
    return list(range(size, 0, -1))


def test_quicksort_performance(sort_function, arr):
    arr_copy = arr.copy()
    start_time = time.time()
    try:
        sort_function(arr_copy, 0, len(arr_copy) - 1)
        end_time = time.time()
        return f"{end_time - start_time:.6f}s"
    except RecursionError:
        return "RecursionError"


if __name__ == "__main__":
    sizes = [100, 300, 500, 700, 900]

    for size in sizes:
        print(f"\nArray size: {size}")

        random_arr = generate_random_array(size)
        sorted_arr = generate_sorted_array(size)
        reverse_arr = generate_reverse_sorted_array(size)

        det_random = test_quicksort_performance(quicksort, random_arr)
        rand_random = test_quicksort_performance(randomized_quicksort, random_arr)

        det_sorted = test_quicksort_performance(quicksort, sorted_arr)
        rand_sorted = test_quicksort_performance(randomized_quicksort, sorted_arr)

        det_reverse = test_quicksort_performance(quicksort, reverse_arr)
        rand_reverse = test_quicksort_performance(randomized_quicksort, reverse_arr)

        print(f"Random input - Deterministic: {det_random}, Randomized: {rand_random}")
        print(f"Sorted input - Deterministic: {det_sorted}, Randomized: {rand_sorted}")
        print(f"Reverse input - Deterministic: {det_reverse}, Randomized: {rand_reverse}")