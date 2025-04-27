#!/c/Users/Nazar/.virtualenvs/pipenv_env/Scripts/python
from sys import argv
import os 
import argparse

import shutil
from datetime import datetime
import my_module

import logging

logger = logging.getLogger(__name__)

logging.basicConfig(filename="logs.log", 
                    level=logging.DEBUG, 
                    encoding='utf-8',
                    format="%(name)s:%(filename)s:%(levelname)s:%(asctime)s:%(message)s")

def call_help():
    logger.info("Ми викликали Help для нашої програми")

def display_version():
    logger.info("Ми вивели версію")

def move_file_to_date_folder(filename: str):
    # Перевіряємо, чи існує файл
    if not os.path.exists(filename):
        logger.warning(f"Файл '{filename}' не знайдено.")
        return

    # Отримуємо поточну дату у форматі YYYY-MM-DD
    date_folder = datetime.now().strftime("%Y-%m-%d")
    logger.info(f"Назва папки буде: {date_folder}")

    # Створюємо папку, якщо вона не існує
    if not os.path.exists(date_folder):
        logger.debug("Створюємо нову папку")
        os.makedirs(date_folder)

    # Переміщуємо файл у папку
    logger.debug("Починаємо Преміщувати файл")
    shutil.move(filename, os.path.join(date_folder, filename))
    logger.info(f"Файл '{filename}' переміщено в папку '{date_folder}'.")

if __name__ == "__main__":
    if False: #argv[0] == "./__main__.py":
        print(f"Запустились, на першій позцї стоїть: {argv[1]}")
        print(f"А на другій {argv[2]}")
    
    #Якщо передали не всі аргументи программа буде падати
    # і нам потрібні винятки 
    # тому придумали бібліотеку argparse

    parser = argparse.ArgumentParser(
        prog="Тестова програма", 
        description="Експерементуємо з аргументами")
    parser.add_argument("-hh", action='store_true', help="Наш тестовий ключ")
    parser.add_argument("-v", "--version", action='store_true', help="Ми додали нашу Версію!")
    parser.add_argument("--filename", type=str, help="Назва файлу для копіювання")
    args = parser.parse_args()

    #print(parser.print_help())
    if args.hh:
        call_help()
    if args.version:
        display_version()
    
    # Приклад виклику функції
    move_file_to_date_folder(args.filename)