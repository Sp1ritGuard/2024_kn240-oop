from multiprocessing import cpu_count
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor, as_completed
from threading import current_thread
from time import sleep, time
import math
import numpy as np

def check_thread(v):
    """Функція для багатопоточночті через треди
    """
    thread = current_thread()
    print(f"{v}: імя потоку={thread.name}")
    a = math.sqrt(64^v)

# with ThreadPoolExecutor() as executor:
#     executor.map(check_thread, range(n_cpu))

def is_prime(n):
    """Перевірка, чи є число простим."""
    print(f"Починаємо визначати чи число {n} є простим.")
    if n <= 1:
        return (n, False)
    if n == 2:
        return (n, True)
    if n % 2 == 0:
        return (n, False)
    sqrt_n = int(math.sqrt(n)) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return (n, False)
    return (n, True)

def gen_matrix(n):
    print(f"Генеруємо матрицю {n}x{n}")
    start = time()
    m = np.random.rand(n, n)
    end = time()
    print(f"Матриця {m.ndim} згенерувалася за {end - start}")
    return n, True

def compute():
    for n in range(100):
        if is_prime(n):
            print("Так просте")
        else:
            print("Ні")

if __name__ == '__main__':
    n_cpu = cpu_count()
    print(f"Кількість процесорів на даному компютері: {n_cpu}")
    with ProcessPoolExecutor() as executor:
        # futures = executor.map(is_prime, range(100))
        futures = executor.map(gen_matrix, range(100, 1000))
        for num, is_prime_resault in futures:
            if is_prime_resault:
                print(f"Число {num} є простим")
            else:
                print(f"Число {num} не є простим")
    
print("Завершення")