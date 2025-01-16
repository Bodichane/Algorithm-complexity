def cocktail_sort(a):
    left = 0
    right = len(a) - 1

    while left <= right:
        # Проход слева направо, аналогично пузырьковой сортировке
        for i in range(left, right):
            if a[i] > a[i + 1]:
                # Если текущий элемент больше следующего, меняем их местами
                a[i], a[i + 1] = a[i + 1], a[i]

        # Уменьшаем правую границу, так как самый большой элемент уже находится на правильной позиции
        right -= 1

        # Проход справа налево
        for i in range(right, left, -1):   
            # Если текущий элемент больше следующего, меняем их местами 
            if a[i] < a[i - 1]:
                a[i], a[i - 1] = a[i - 1], a[i]

        # Увеличиваем левую границу, так как самый маленький элемент уже находится на правильной позиции
        left += 1
    return a

# Пример использования:
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = cocktail_sort(unsorted_list)
print(sorted_list)