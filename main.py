# Любая функция в Python обозначается как def
def sumNumbers(n):  # sumNumbers - название функции. Принимает один аргумент (n).
    summa = 0
    for i in range(1, n+1):
        summa += i
    print(summa)

sumNumbers(5)

В этом случае функция будет возвращать значение:
def sumNumbers(n):
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
a = sumNumbers(5)
print(a)
# Функция завершает свою работу, когда видет оператор return.

В этом случае функция принимает 2 аргумента:
def sumNumbers(n, y = 'Hello'):
    print(y)
    summa = 0
    for i in range(1, n+1):
        summa += i
    return summa
a = sumNumbers(5, 'qwerty')
print(a)
# Если не задать второй аргумент, то функция будет использовать второй агрумент поумолчанию (Hello)

# Чтобы указать Пайтону, что мы хотим передать неограниченное колличество аргументов, нужно поставить *
def sum_str(*args):
    res = ''
    for i in args:
        res += i
    return res

print(sum_str('q', 'e', 'l'))
print(sum_str('q', 'e', 'l', 'r', 'f'))


# МОДУЛЬ - это файл, в котором находятся различные функции, которые мы можем использовать.
# Чтобы импортировать функции из модуля, сперва нужно импортировать сам модуль.
import modul1

print(modul1.max1(5, 9))

# Так можно напрямую обратиться к определённой функции, не вызывая весь модуль:
from modul1 import max1

print(max1(10, 9))

# С помощью * можно импортировать все функции из модуля, не импортируя сам модуль
from modul1 import *

print(max1(10, 12))

# Так можно изменить имя модуля внутри программы:
import modul1 as m1

print(m1.max1(14, 12))


# РЕКУРСИЯ - это функция вызывающая саму себя.
# При создании рекурсии всегда нужно указывать базис - то место,
# когда функция будет останавливаться и рекурсия завершаться.

# Пользователь вводит число n. Необходимо вывести n - первых чисел последовательности Фибоначчи.
def fib(n):
    if n in [1, 2]:  # если перенная n будет находиться в списке 1, 2 - возвращать единицу. Это базис рекурсии.
        return 1
    return fib(n-1) + fib(n-2)

list_1 = []
for i in range(1, 10):
    list_1.append(fib(i))
print(list_1)


# АЛГОРИТМЫ - это наборы инструкций для выполнения некоторой задачи.

# Быстрая сортировка:
def quick_sort(array):
    if len(array) <= 1:
        return array
    else:
        pivot = array[0]
    less = [i for i in array[1:] if i <= pivot]
    greater = [i for i in array [1:] if i > pivot]
    return quick_sort(less) + [pivot] + quick_sort(greater)

print(quick_sort([14,5,9,6,3,58,7,5,2,7]))

# Сортировка слиянием:
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1

list1 = [1,5,6,9,8,7,2,1,55,2,4]
merge_sort(list1)
print(list1)