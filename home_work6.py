# --- Задача №1 Фильтрация данных ---
def check_length(city_name): # Возвращает False, если длина строки меньше трех символов, иначе True
    return len(city_name) >= 3

def filter_cities(cities): # Возвращает список городов длиной не менее трех символов.
    return list(filter(check_length, cities)) # Фильтруем данные используя filter и функцию check_length

def task_1(): # Функция ввода исходных данных и вывода результата
    cities_input = input("Введите названия городов, разделенных пробелом: ") # Ввод списка названий городов
    print(f'Исходный список городов: {cities_input}')
    filtered_cities = filter_cities(cities_input.split()) # Преобразуем в список и применяем фильтрацию
    print(f'Города длиной не менее трех символов: {filtered_cities}') # Вывод результата
    
# Проверка
if __name__ == "__main__":
    task_1()

# --- Задача №2 Вложенные функции ---
def get_list(input_string): # Принимает строку и возвращает список чисел
    return list(map(int, input_string.split()))  # Преобразуем строку в список

def sort_func(func): # Принимает функцию и сортирует результат
    result = func()  # Вызываем переданную функцию
    return sorted(result)  # Сортируем результат и возвращаем

def task_2(): # Функция ввода исходных данных и вывода результата
    input_string = input("Введите целые числа, разделенные пробелами: ") # Ввод строки с целыми числами
    print(f'Исходный список чисел: {input_string}')
    sorted_numbers = sort_func(lambda: get_list(input_string))  # Вызываем sort_func с get_list как аргумент через lambda функцию
    print(f'Отсортированный список чисел: {sorted_numbers}') # Вывод результата
    
# Проверка
if __name__ == "__main__":
    task_2()

# --- Задача №3 Перестановки строк ---
import itertools
def get_permutations(s, n): # Перестановки
    perms = itertools.permutations(s, n) # генерирует перестановки длинной n
    unique_perms = set([''.join(p) for p in perms]) # Преобразуем кортежи обратно в строки и удаляем дубликаты
    sorted_perms = sorted(unique_perms) # Сортируем уникальные перестановки в лексикографическом порядке
    return sorted_perms

def task_3 (): # Функция ввода исходных данных и вывода результата
    input_string = input("Введите строку: ") # ВВод строки
    n = int(input("Введите количество символов для перестановки: ")) # Ввод количества символов для перестановки
    result = get_permutations(input_string, n) # вызываем функцию перестановки
    print(f'Перестановки в лексикографическом порядке строки {input_string}, кол-во символов: {n}') # Вывод результата
    print(result)
    
# Проверка
if __name__ == "__main__":
    task_3()
    
# --- Задача №4 Комбинации символов ---
import itertools
 
def get_combinations(s, k): # Комбинирует символы
    all_combinations = []
    for i in range(1, k + 1): # Цикл от 1 до k
        combinations = itertools.combinations(s, i) # считаем комбинации длинны i
        all_combinations.extend([''.join(combo) for combo in combinations]) # Добавляем в список
    return all_combinations

def task_4(): # Функция ввода данных и вывода результата
    input_string = input("Введите строку: ") # Ввод строки
    k = int(input("Введите максимальную длину: ")) # Ввод длинны
    result = get_combinations(input_string, k) # Вызываем функцию комбинации символов
    print(f'Возможные комбинации строки {input_string} c длинной <= {k}') # Вывод результата
    print(result)
    
# Проверка
if __name__ == "__main__":
    task_4()
    
# --- Задача №5 Функция с частичными аргументами ---
from functools import partial

def sort_users_by_age(users, reverse=False):  # возвращает сортированный список пользователей
    return sorted(users, key=lambda user: user['age'], reverse=reverse)

# Создание частичных функций для сортировки
sort_by_age_asc = partial(sort_users_by_age, reverse=False)  # Сортировка по возрастанию

sort_by_age_desc = partial(sort_users_by_age, reverse=True)  # Сортировка по убыванию

def task_5(users): # Функция вывода результата
    print(f'Сортировка по возрастанию: {sort_by_age_asc(users)}')
    print(f'Сортировка по убыванию: {sort_by_age_desc(users)}')
# Проверка
if __name__ == "__main__":
    # Словарь с пользователями и возрастом
    users = [
    {'name': 'Василий', 'age': 30},
    {'name': 'Ольга', 'age': 25},
    {'name': 'Иван', 'age': 50},
    ] 
    task_5(users)