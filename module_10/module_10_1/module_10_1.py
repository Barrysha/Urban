import requests
from datetime import datetime
from threading import Thread
from time import sleep

time_start = datetime.now()

def write_words(word_count, file_name):
    time_start_func = datetime.now()
    with open(file_name, 'w') as output_file:
        for i in range(word_count):
            output_file.write(f"Какое-то слово №{i}\n")
            sleep(0.1)
    time_res = datetime.now() - time_start_func
    print(f"Завершилась запись в файл {file_name} \nВремя выполнения {time_res}")

write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')

thread1 = Thread(target=write_words, args=(10, 'example5.txt'))
thread2 = Thread(target=write_words, args=(30, 'example6.txt'))
thread3 = Thread(target=write_words, args=(200, 'example7.txt'))
thread4 = Thread(target=write_words, args=(100, 'example8.txt'))

thread1.start()
thread2.start()
thread3.start()
thread4.start()

thread1.join()
thread2.join()
thread3.join()
thread4.join()

time_end = datetime.now()
time_result = time_end - time_start

print('', time_start, '\n', time_end, '\n',time_result)
