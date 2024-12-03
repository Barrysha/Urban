import requests
from datetime import datetime
from threading import Thread


time_start = datetime.now()
THE_URL = 'https://api.github.com'
res = []


def func(url):
    response = requests.get(THE_URL)
    page_response = response.json()
    res.append(page_response)

thr_first = Thread(target=func, args=(THE_URL, ))
thr_second = Thread(target=func, args=(THE_URL, ))
thr_third = Thread(target=func, args=(THE_URL, ))
thr_first.start()
thr_second.start()
thr_third.start()

thr_first.join()
thr_second.join()
thr_third.join()

time_end = datetime.now()
print(res, '\n', time_start, '\n', time_end, '\n', time_end - time_start)
