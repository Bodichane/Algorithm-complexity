def bubble_sort(a):
    n = len(a)

    # Внешний цикл проходит по всем элементам массива
    for i in range(n - 1):
        for j in range(n - 1, i, -1):
            # Сравниваем соседние элементы
            if a[j] < a[j - 1]:
                # Если текущий элемент больше следующего, меняем их местами
                a[j], a[j - 1] = a[j - 1], a[j]
    return a

# Пример использования:
unsorted_list = [64, 25, 12, 22, 11]
sorted_list = bubble_sort(unsorted_list)
print("Отсортированный список:", sorted_list)