def quick_sort(a):
    if len(a) <= 1:
        return a
     
    q = a[len(a) // 2] # Выбор опорного элемента

    # Разделение массива на три части: элементы меньше, равные и больше опорного
    left = [x for x in a if x < q]
    middle = [x for x in a if x == q]
    right = [x for x in a if x > q]
    
    # Рекурсивное объединение результатов
    return quick_sort(left) + middle + quick_sort(right)

# Пример использования:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = quick_sort(unsorted_list)
print(sorted_list)