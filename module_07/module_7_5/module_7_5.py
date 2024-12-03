import os
from time import strftime, localtime
# Работаю на линуксе. Не могу использовать os.startfile(), буду признателен, если подскажите решение. Интернет пока не шибко помог. Спасибо!
d = '.'

# print("Текущая директория:", os.getcwd())
# if os.path.exists("module_7_5_papka"):
#     os.chdir("module_7_5_papka")
# else:
#     os.mkdir("module_7_5_papka")
#     os.chdir("module_7_5_papka")

# print("Текущая директория:", os.getcwd())
# #os.makedirs("second/third")
#
# os.chdir("/home/barry/Рабочий стол/Python/Домашка/Задания/module_7/module_7_5")
# print("Текущая директория:", os.getcwd(), '\n')

# files = [f for f in os.listdir() if os.path.isfile(f)]
# dirs = [d for d in os.listdir() if os.path.isdir(d)]

# print('', os.listdir(), '\n', files, '\n', dirs, '\n')

# print(os.stat(files[1]))

# print(os.listdir(), '\n')
for root, dirs, files in os.walk(d):
    for f in files:
        filepath = os.path.join(root, f)
        filetime = os.path.getmtime(filepath)
        formtime = strftime("%d.%m.%Y.%H:%M", localtime(filetime))
        filesize = os.path.getsize(filepath)
        parentdir = os.path.dirname(filepath)
        print(f"Обнаружен файл: {f}, путь: {filepath}, размер: {filesize} байт, время изменения: {formtime}, родительская директория: {parentdir}", '\n')



