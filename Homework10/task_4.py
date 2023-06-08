# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import time

import pytest


@pytest.mark.usefixtures("class_fixture")
class Test:

    def test_1(self):
        time.sleep(1)

    def test_2(self, func_fixture):
        time.sleep(1.5)

    def test_3(self):
        time.sleep(2)
