import random

array_size = 8
random_array = [random.randint(1, 100) for _ in range(array_size)]
print("Исходный массив:", random_array)

def bubble_sort(arr):
    n = len(arr)
    for run in range (n - 1):
        for i in range(n -1- run):
            if arr[i] >= arr[i+1]:
                arr[i],arr[i+1] = arr[i+1], arr[i]

bubble_sorted = random_array
bubble_sort(bubble_sorted)
print("Отсортированный с Bubble:  ", bubble_sorted)

def selection_sort(arr):
    for num in range(len(arr)):
        min_vallue = num

        for i in range(num, len(arr)):
            if arr[min_vallue] > arr[i]:
                min_vallue = i

        arr[num], arr[min_vallue] = arr[min_vallue], arr[num]

selection_sorted = random_array
selection_sort(selection_sorted)
print("Отсортированный с selection:  ", selection_sorted)

def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        current_value = arr[i]
        position = i - 1
        while position >= 0 and current_value < arr[position]:
            arr[position + 1] = arr[position]
            position -= 1
        arr[position + 1] = current_value

insertion_sorted = random_array
insertion_sort(insertion_sorted)
print("Отсортированный с insertion:  ", insertion_sorted)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    first_array = arr[:mid]
    second_array = arr[mid:]

    first_array = merge_sort(first_array)
    second_array = merge_sort(second_array)

    result = []
    while first_array and second_array:
        if first_array[0] <= second_array[0]:
            result.append(first_array.pop(0))
        else:
            result.append(second_array.pop(0))

    while first_array:
        result.append(first_array.pop(0))
    while second_array:
        result.append(second_array.pop(0))

    return result

sorted_megre = random_array
merge_sort(sorted_megre)
print("Отсортированный с merge:  ", sorted_megre)



