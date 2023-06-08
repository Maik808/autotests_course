import pytest
import datetime


@pytest.fixture(scope="class")
def class_fixture():
    # время начала выполнения тестов в классе
    start_time = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
    print('Время старта тестового класса ', start_time)
    yield
    # время окончания выполнения тестов в классе
    end_time = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
    print('Время окончания работы тестового класса', end_time)


@pytest.fixture(scope="function")
def func_fixture():
    # время начала выполнения одного теста
    start_time = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
    print('Время старта теста ', start_time)
    yield
    # время окончания выполнения одного теста
    end_time = datetime.datetime.now().strftime('%d.%m %H:%M:%S')
    print('Время окончания работы теста ', end_time)
