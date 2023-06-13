# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize('a, b, result', [
    pytest.param(50, 10, 5, marks=pytest.mark.smoke),
    pytest.param(-30, '-3', -2, marks=pytest.mark.skip('Skip this parameter set')),
    (-30, -3, 10)],
                         ids=['positive', 'invalid_variable', 'negative'])
def test(a, b, result):
    assert all_division(a, b) == result
