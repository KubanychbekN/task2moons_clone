import random

# Создаем массив с рандомными данными
array_size = 10
random_array = [random.randint(1, 100) for _ in range(array_size)]
print("Исходный массив:", random_array)

# Buble Sort (Сортировка пузырьком)
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

bubble_sorted = random_array.copy()
bubble_sort(bubble_sorted)
print("Отсортированный пузырьком:", bubble_sorted)

# Selection Sort (Сортировка выбором)
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

selection_sorted = random_array.copy()
selection_sort(selection_sorted)
print("Отсортированный выбором:", selection_sorted)

# Insertion Sort (Сортировка вставкой)
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

insertion_sorted = random_array.copy()
insertion_sort(insertion_sorted)
print("Отсортированный вставкой:", insertion_sorted)

# Merge Sort (Сортировка слиянием)
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

merge_sorted = random_array.copy()
merge_sort(merge_sorted)
print("Отсортированный слиянием:", merge_sorted)
