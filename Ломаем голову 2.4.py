# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. 
# Найдите произведение элементов на указанных позициях. 
# Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число N: '))
f = -n
i = 1
print('Произведение нечётных чисел: ')
while (f<n):
    # print(f'{f} ', end='')
    f = f + 1
    if f % 2 == 1:
        i = i*f
print(f'{i} ', end='')


Я знаю, что задание звучит немного иначе, но пока что не разобралась как сделать ввод индекса чисел с клавиатуры через пробел.
