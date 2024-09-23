from time import sleep
from datetime import datetime
from threading import Thread


def write_words(word_count, file_name):
    file = open(file_name, 'a', encoding='utf-8')
    for i in range(word_count):
        file.write('Какое-то слово № {i+1} \n')
        sleep(0.1)
    file.close()
    print(f'Завершилась запись в файл {file_name}')

time_start = datetime.now()


write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
time_stop = datetime.now()
time_res = time_stop - time_start
print(f'Время выполнения функции {time_res}')


time_start2 = datetime.now()

thr_first = Thread(target=write_words, args=(10, 'example1.txt'))
thr_second = Thread(target=write_words, args=(30, 'example2.txt'))
thr_third = Thread(target=write_words, args=(200, 'example3.txt'))
thr_fourth = Thread(target=write_words, args=(100, 'example4.txt'))
thr_first.start()
thr_second.start()
thr_third.start()
thr_fourth.start()

thr_first.join()
thr_second.join()
thr_third.join()
thr_fourth.join()
time_stop2 = datetime.now()
time_res2 = time_stop2 - time_start2
print(f'Время выполнения потоков {time_res2}')