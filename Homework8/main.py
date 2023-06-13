def treatment_sum(our_tuple):
    """
    Функция складывает и возвращает данные, корректно обрабатывая исключения

    """
    try:
        if len(our_tuple) == 2:
            return our_tuple[0] + our_tuple[1]
        elif len(our_tuple) > 2:
            raise Exception('Много данных')

    except IndexError:
        return 'Недостаточно данных'
    except TypeError:
        return 'Нельзя сложить эти данные'


data = (3, '5')
print(treatment_sum(data))
