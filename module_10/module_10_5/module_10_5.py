import time
from multiprocessing import Pool

def read_info(name):
    all_data = []
    with open(name, 'r', encoding='utf-8') as f:
        while True:
            string = f.readline()
            if string == '':
                break
            all_data.append(string)

if __name__ == '__main__':
    filenames = [f'Files/file {number}.txt' for number in range(1, 5)]

    # Линейный
    start_time = time.time()
    for filename in filenames:
        read_info(filename)
    end_time = time.time()
    print(f'{end_time - start_time} (линейный)')

    # Многопроцессный
    start_time = time.time()
    with Pool() as pool:
        pool.map(read_info, filenames)
    end_time = time.time()
    print(f'{end_time - start_time} (многопроцессный)')
