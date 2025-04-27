import csv
import string
import random
from tqdm import tqdm
from time import sleep
import psutil
import os

def get_memory_usage():
    process = psutil.Process(os.getpid())
    return process.memory_info().rss / 1024 / 1024  # в MB

if __name__ == "__main__":
    print(f"Початкова памʼять: {get_memory_usage():.2f} MB")

    os.remove("1.csv")
    with(open("1.csv", 'a')) as f:
        wr = csv.writer(f)
        for i in range(1000):
            ss = "".join(random.choices(string.ascii_letters, k = 3))
            wr.writerow([random.choice(string.digits), "tt", 0, ss])

    print(f"Після запису файлу: {get_memory_usage():.2f} MB")

    def get_csv():
        with open("1.csv") as c:
            rw = csv.reader(c)
            for i, r in enumerate(rw):
                # Перше: номер рядка, друге: власне значення
                yield i, r

    for i, s in tqdm(get_csv(), total=1000):
            # print(f"Читаємо стрічку {s} під номером {i}")
        sleep(0.01)
    # print(len(list(get_csv())))

    print(f"Після читання файлу: {get_memory_usage():.2f} MB")