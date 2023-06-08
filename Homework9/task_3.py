# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код

with open('test_file/task_3.txt', 'r') as f:
    x = 0
    sum_list = []
    for one_line in f.readlines():
        if len(one_line) > 2:
            x += int(one_line[:-1])
        else:
            sum_list.append(x)
            x = 0
sum_list.sort()
three_most_expensive_purchases = sum(sum_list[-3:])

assert three_most_expensive_purchases == 202346
