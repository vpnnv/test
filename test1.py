def binary_search(arr, x):
    """
    Реализация алгоритма двоичного поиска.
    """
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            return mid
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return low


def sort_list(arr):
    """
    Функция сортировки списка по возрастанию элементов.
    """
    return sorted(arr)


input_list = input("Введите список чисел через пробел: ").split()

try:
    # Преобразуем введенную строку в список целых чисел
    input_list = list(map(int, input_list))

    # Сортируем список по возрастанию элементов
    sorted_list = sort_list(input_list)

    # Запрашиваем у пользователя число для поиска позиции
    x = int(input("Введите число для поиска позиции: "))

    # Ищем позицию элемента в списке с помощью двоичного поиска
    pos = binary_search(sorted_list, x)

    # Выводим результат
    if pos == len(sorted_list):
        print("Число больше всех элементов в списке")
    elif pos == 0 and x < sorted_list[0]:
        print("Число меньше всех элементов в списке")
    else:
        print(f"Позиция элемента, который меньше {x}, а следующий за ним больше или равен этому числу: {pos}")

except ValueError:
    print("Ошибка: введены некорректные данные. Введите только целые числа через пробел.")