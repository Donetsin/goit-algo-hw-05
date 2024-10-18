def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    mid = 0
    iteration = 0

    while low <= high:
        iteration += 1
        mid = (high + low) // 2

        # x присутній на позиції і
        if arr[mid] == x:
            return (iteration, mid)

        # x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1

        # x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            high = mid - 1

    if low < len(arr):
        return (iteration, low)

    return (iteration, 'None')


# Приклад використання:
arr = [1.1, 2.2, 3.3, 4.4, 5.5, 6.6, 7.7, 8.8, 9.9]
x = 4.5

search_result = binary_search(arr, x)
print(search_result)
