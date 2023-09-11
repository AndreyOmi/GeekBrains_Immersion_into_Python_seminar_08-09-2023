'''
Задача № 4: Создайте функцию генератор чисел Фибоначчи (см. Википедию).
'''

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

# Создание генератора

fibonacci = fibonacci_generator()

# Использование генератора для получения первых 15 чисел Фибоначчи

for _ in range(15):
    print(next(fibonacci))
