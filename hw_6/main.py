from faker import Faker
import random

fake = Faker()

# Эта библиотека нужна для генерации случайных данных и тестов.
# Здесь мы используем её для генерации случайных чисел для списка.
nums = [random.randint(1, 20) for _ in range(10)]  # список из 10 случайных чисел
target = random.randint(10, 25)  # случайная цель

print("Список чисел:", nums)
print("Цель (target):", target)

# 🔹 Алгоритм Two Sum (вложенные циклы)
result = []
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            result = [i, j]

if result:
    print("Индексы чисел, сумма которых равна target:", result)
    print("Значения чисел:", [nums[result[0]], nums[result[1]]])
else:
    print("Нет двух чисел, сумма которых равна target")