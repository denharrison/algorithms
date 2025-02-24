# Пример рекурсии 
def factorial_recursive(n):
 """
 Вычисляет факториал числа n рекурсивно.

 Args:
  n: Целое неотрицательное число.

 Returns:
  Факториал числа n. Возвращает 1, если n равно 0.
  Возвращает ошибку ValueError, если n отрицательное.
 """
 if n < 0: # Базовый случай: Обработка отрицательных чисел.
  raise ValueError("Факториал не определен для отрицательных чисел")
 elif n == 0: # Базовый случай: Факториал 0 равен 1.
  return 1
 else: # Рекурсивный случай: n! = n * (n-1)!
  return n * factorial_recursive(n - 1) # Рекурсивный вызов функции самой себя

# Пример использования:
try:
 print(factorial_recursive(5)) # Вывод: 120
 print(factorial_recursive(0)) # Вывод: 1
 print(factorial_recursive(-2)) # Вывод: ValueError: Факториал не определен для отрицательных чисел
except ValueError as e:
  print(e)



# Функция `factorial_recursive(n)` вычисляет факториал числа `n`.
# Базовый случай: Если `n` равно 0, функция возвращает 1 (факториал 0 равен 1). 
# Это необходимо, чтобы рекурсия завершилась. Без базового случая функция будет вызывать себя бесконечно.
# Рекурсивный случай: Если `n` больше 0, функция возвращает `n` умноженное на результат вызова `factorial_recursive(n-1)`. 
# Это рекурсивный вызов: функция вызывает себя же, но с меньшим аргументом. 
# Этот процесс продолжается до тех пор, пока не будет достигнут базовый случай (`n == 0`).



# Итеративный пример 
def factorial_iterative(n):
 """
 Вычисляет факториал числа n итеративно.

 Args:
  n: Целое неотрицательное число.

 Returns:
  Факториал числа n. Возвращает 1, если n равно 0.
  Возвращает ошибку ValueError, если n отрицательное.
 """
 if n < 0:
  raise ValueError("Факториал не определен для отрицательных чисел")
 elif n == 0:
  return 1
 else:
  result = 1 # Инициализация результата
  for i in range(1, n + 1): # Цикл от 1 до n (включительно)
   result *= i # Умножаем текущий результат на i
  return result

# Пример использования:
try:
  print(factorial_iterative(5)) # Вывод: 120
  print(factorial_iterative(0)) # Вывод: 1
  print(factorial_iterative(-2)) # Вывод: ValueError: Факториал не определен для отрицательных чисел
except ValueError as e:
  print(e)


# Функция `factorial_iterative(n)` вычисляет факториал числа `n` с помощью цикла `for`.
# Она инициализирует переменную `result` значением 1.
# Цикл проходит по числам от 1 до `n` (включительно) и умножает `result` на каждое число.
# В конце цикла `result` содержит факториал `n`.
