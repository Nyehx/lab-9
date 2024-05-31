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
    template1 = ["One", "Two", "Three", "Four"]
    arr1 = ["One", "Three", "Three", "Three", "Two"]
    assert counting_sort_strings(arr1, template1) == ["One", "Two", "Three", "Three", "Three"]
    print("Тест 1 пройден")

    # Тест 2: Строки на разных языках
    template2 = ["Один", "Два", "Three", "Four"]
    arr2 = ["Three", "Four", "Один", "Два", "Three"]
    assert counting_sort_strings(arr2, template2) == ["Один", "Два", "Three", "Three", "Four"]
    print("Тест 2 пройден")

    # Тест 3: Пустой массив
    template3 = ["Один", "Два", "Три"]
    arr3 = []
    assert counting_sort_strings(arr3, template3) == []
    print("Тест 3 пройден")

    print("Все тесты пройдены")

test()
