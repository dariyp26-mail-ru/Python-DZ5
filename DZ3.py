# Задача 3. Задайте список случайных чисел от 1 до 10. Посчитайте, сколько всего совпадающих элементов есть в списке. Удалите все повторяющиеся элементы.
# [1, 4, 2, 3, 4, 6, 1, 7] => 4 элемента совпадают Список уникальных элементов
# [1, 4, 2, 3, 6, 7]

import random
rnd = random.randint(5, 15)
numbers = [random.randint(1, 10) for i in range(rnd)]
print(numbers)

print('Список уникальных элементов:')
non_repeat_numbers = list(filter(lambda x: numbers.count(x) == 1, numbers))
print(non_repeat_numbers)

count = len(numbers) - len(non_repeat_numbers)
print('Элементов совпадает:', count)
