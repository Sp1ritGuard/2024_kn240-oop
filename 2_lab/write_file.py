import os
import random
import string
import time
from threading import Thread
from concurrent.futures import ThreadPoolExecutor

def generate_random_text(length=100, words=True):
    """
    Генерує випадковий текст.
    :param length: Довжина тексту або кількість слів
    :param words: Чи використовувати слова (True) або просто символи (False)
    :return: Згенерований рядок
    """
    if words:
        word_list = ["".join(random.choices(string.ascii_letters, k=random.randint(3, 10))) for _ in range(length)]
        return " ".join(word_list)
    else:
        return "".join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))

def write_random_to_file(filename, text_length=100, use_words=True):
    """
    Створює файл, записує в нього випадковий текст.
    :param filename: Назва файлу
    :param text_length: Довжина випадкового тексту
    :param use_words: Використовувати слова або окремі символи
    """
    print(f"Створюємо файл {filename}")
    with open(filename, 'w', encoding='utf-8') as file:
        time.sleep(random.randint(1,5))
        file.write(generate_random_text(text_length, use_words))
    print(f"Файл '{filename}' успішно створено та заповнено випадковими даними.")

if __name__ == "__main__":
    
    text_length = int(50)
    use_words = True
    
    start = time.time()
    tl = list()
    #for i in range(5):
    #    filename = f"data_{i}.txt"
    #    t = Thread(target=write_random_to_file, args=[filename, text_length, use_words])
    #    #write_random_to_file(filename, text_length, use_words)
    #    tl.append(t)
    #    t.start()
    #    print(f"Запустили тред для файла {filename}")
    
    #for j in tl:
    #    j.join()
    #    print("Зібрали результати")
    
    end = time.time()
    print(f"Генерації файла зайняла {end-start}")

    # Пробуємо Екзеклютор для тредів
    start = time.time()
    with ThreadPoolExecutor(max_workers=2) as executor:
        arguments = [f"data_{i}.txt" for i in range(5)]
        for _ in executor.map(write_random_to_file, arguments):
            print(_)
    

    end = time.time()
    print(f"Генерації файлів зайняла {end-start}")