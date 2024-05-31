def counting_sort_strings(arr, temp, ascending=True):
    count = {s: 0 for s in temp}
    for s in arr:
        count[s] += 1

    new_arr = []
    if ascending:
        for s in temp:
            new_arr.extend([s] * count[s])
    else:
        for s in reversed(temp):
            new_arr.extend([s] * count[s])

    return new_arr

def test():
    # Тест 1: Массив строк разных длин
    template1 = ["apple", "banana", "cherry", "date"]
    arr1 = ["banana", "apple", "cherry", "banana", "date", "apple", "cherry"]
    assert counting_sort_strings(arr1, template1) == ["apple", "apple", "banana", "banana", "cherry", "cherry", "date"]
    print("Тест 1 пройден")

    # Тест 2: Строки на разных языках
    template2 = ["привет", "здравствуйте", "hello", "bonjour"]
    arr2 = ["hello", "привет", "bonjour", "здравствуйте", "привет", "hello"]
    assert counting_sort_strings(arr2, template2) == ["привет", "привет", "здравствуйте", "hello", "hello", "bonjour"]
    print("Тест 2 пройден")

    # Тест 3: Пустой массив
    template3 = ["apple", "banana", "cherry"]
    arr3 = []
    assert counting_sort_strings(arr3, template3) == []
    print("Тест 3 пройден")

    # Тест 4: Сортировка по убыванию
    template4 = ["apple", "banana", "cherry", "date"]
    arr4 = ["banana", "apple", "cherry", "banana", "date", "apple", "cherry"]
    assert counting_sort_strings(arr4, template4, ascending=False) == ["date", "cherry", "cherry", "banana", "banana",
                                                                       "apple", "apple"]
    print("Тест 4 пройден")

    print("Все тесты пройдены успешно!")

test()
