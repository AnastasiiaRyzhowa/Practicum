import os # позволяют определять тип операционной системы, получать доступ к переменным окружения, управлять директориями и файлами:
import shutil #работать с файловым объектом и предлагает нам возможность копировать и удалять файлы
from pathlib import Path

menu = '''
1. Создание папки (с указанием имени);
2. Удаление папки по имени;
3. Перемещение между папками (в пределах рабочей папки) - заход в папку по имени, выход на уровень вверх;
4. Создание пустых файлов с указанием имени;
5. Запись текста в файл;
6. Просмотр содержимого текстового файла;
7. Удаление файлов по имени;
8. Копирование файлов из одной папки в другую;
9. Перемещение файлов;
10. Переименование файлов.
11. Выход из программы
'''


def create_folder(name): #Создание каталога и установка режима доступа к нему.
    os.mkdir(name)


def delete_folder(name): #Удаление папки независимо от того, содержит ли она файлы, доступные только для чтения
    shutil.rmtree(name, ignore_errors=True)


def move_to_folder(path, root_folder):
    while True:
        os.chdir(input("Введите имя папки, в которую хотите перейти, или путь: ")) #Смена рабочей директории из кода
        if root_folder in os.getcwd().split('/'):
            break
        else:
            print("Нельзя выходить из корневой папки")


def create_file(file_name): # Создание пустых файлов с указанием имени
    with open(file_name, "w", encoding="utf-8") as file:
        file.write


def write_file(file_name): #Запись текста в файл
    with open(file_name, "w", encoding="utf-8") as file:
        file.write(input("Введите текст, который хотите написать: "))


def read_file(file_name): #Просмотр содержимого текстового файла
    with open(file_name, "r", encoding="utf-8") as file:
        lines = file.readlines()
        print(f"Файл {file_name} содержит: ")
        for line in lines:
            print(line)


def remove_file(file_name): # Удаление файлов по имени
    os.remove(file_name)


def copy_file():
    file_name = input("Введите название файла, который хотите скопировать: ")
    dict_name = input("Укажите в какую папку хоитите скопировать или путь: ")
    shutil.copy(file_name, dict_name) # Копирование файлов из одной папки в другую


def move_file():
    file_name = input("Введите название файла, который хотите скопировать: ")
    dict_name = input("Укажите в какую папку хоитите скопировать или путь: ")
    shutil.move(file_name, dict_name) # Перемещение файлов;


def rename_file():
    file_name = input("Введите название файла, который хотите переименовать: ")
    new_file_name = input("Введите новое название файла: ")
    os.rename(file_name, new_file_name) #Выход из программы


print("Настройка: Сначала укажите папку, в которой будем работать")


path = input("Введите путь к папке: ")
os.chdir(path)
root_folder = os.getcwd().split('/')[-1]

while True:
    print("Текущие файлы", os.listdir())
    print(menu)
    command = int(input("Выбирите пункт в меню: "))
    if command == 1:
        name = input("Введите имя папки: ")
        create_folder(name)
    if command == 2:
        name = input("Введите имя папки: ")
        delete_folder(name)
    if command == 3:
        move_to_folder(path, root_folder)

    if command == 4:
        file_name = input("Введите название файла: ")
        create_file(file_name)

    if command == 5:
        file_name = input("Введите название файла: ")
        write_file(file_name)

    if command == 6:
        file_name = input("Введите название файла: ")
        read_file(file_name)

    if command == 7:
        file_name = input("Введите название файла: ")
        remove_file(file_name)

    if command == 8:
        copy_file()

    if command == 9:
        move_file()

    if command == 10:
        rename_file()

    if command == 11:
        break
