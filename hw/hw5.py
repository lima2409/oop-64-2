import time

def timer(func):
    def wrapper():
        start = time.time()      # начало
        func()                   # выполнение функции
        end = time.time()        # конец
        print(f"Время выполнения: {round(end - start, 2)} секунд")
    return wrapper


@timer
def download_video():
    time.sleep(2)
    print("Видео загружено")


download_video()