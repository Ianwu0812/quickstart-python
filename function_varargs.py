def total(a=52, *numbers, **phonebook):
    print(a, a)

    # 遍曆元組中的所有項目
    for single_item in numbers:
        print('single_item', single_item)

    # 遍歷字典中的所有項目
    for first_part, second_part in phonebook.items():
        print(first_part, second_part)

print(total(10, 1, 2, 3, Jack=1123, John=2231, Inge=1560))

