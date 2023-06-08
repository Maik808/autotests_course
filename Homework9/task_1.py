# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код
from pathlib import Path

path_read = Path("test_file/task1_data.txt")  # относительный путь
abs_path_read = Path(Path.cwd(), path_read)  # абсолютный путь до файла для чтения

with open(abs_path_read, mode='r', encoding='utf-8') as f:
    f = list(f)
    new = ''
    for item in f:
        for y in item:
            if not y.isdigit():
                new += y

path_write = Path("test_file/task1_answer.txt")  # относительный путь
abs_path_write = Path(Path.cwd(), path_write)  # абсолютный путь до файла для записи

with open(abs_path_write, "w", encoding='utf-8') as file:
    file.write(new)

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
