# Звіт до лабораторної роботи №4

## Тема: **Віртуальні середовища в Python**

## Мета роботи:
Ознайомлення з концепцією віртуальних середовищ у Python, вивчення процесу встановлення та використання сторонніх бібліотек, а також інструментів для керування залежностями.

## Теоретичні відомості

Ізольовані віртуальні середовища в Python — це окремі середовища, що містять власні версії інтерпретатора Python, встановлені бібліотеки та скрипти. Такі середовища дозволяють працювати над різними проєктами без конфліктів між залежностями, що особливо важливо для підтримки сумісності різних версій бібліотек.

## Основи роботи зі сторонніми бібліотеками

Перед початком роботи із сторонніми бібліотеками необхідно переконатися в наявності менеджера пакетів `pip`, який дозволяє встановлювати, оновлювати та видаляти пакети.

### Перевірка наявності pip

Виконано команди:
```bash
pip -V
pip --help
```
Результат показав, що pip успішно встановлений.

### Огляд основних команд pip:

- **install** — встановлення пакетів;
- **uninstall** — видалення пакетів;
- **freeze** — вивід встановлених пакетів у форматі requirements;
- **list** — список встановлених пакетів;
- **show** — інформація про пакет;
- **check** — перевірка сумісності залежностей;
- **search** — пошук пакетів у PyPI;
- інші допоміжні команди (cache, debug, config).

### Перелік встановлених бібліотек:

| Бібліотека         | Версія   | Опис |
|---------------------|----------|------|
| pip                 | 24.3.1   | Менеджер пакетів Python |
| setuptools          | 75.8.0   | Інструменти для створення пакетів |
| requests            | 2.32.3   | HTTP-запити |
| httpx               | 0.28.1   | Асинхронні HTTP-запити |
| numpy               | 2.2.2    | Наукові обчислення |
| ipykernel           | 6.29.5   | Підтримка Jupyter |
| ipython             | 8.31.0   | Інтерактивний інтерпретатор |
| ...                 | ...      | ... |


## Практична частина

### Встановлення та тестування бібліотеки `requests`

Встановлення:
```bash
pip install requests
```

Перевірка роботи:
```python
import requests
r = requests.get('https://google.com')
print(f"Повернув статус: {r.status_code}")
```

Результат:
```
Повернув статус: 200
```
### Основні методи бібліотеки requests:

- `requests.get(url)` — отримання даних;
- `requests.post(url, data)` — надсилання даних;
- `requests.put(url, data)` — оновлення ресурсу;
- `requests.delete(url)` — видалення ресурсу;
- інші спеціалізовані запити (`head`, `options`, `patch`).

### Оновлення та видалення бібліотеки requests

Оновлення:
```bash
pip install "requests>=2.26"
```

Видалення:
```bash
pip uninstall requests
```

**Важливо:** встановлення старих версій може викликати проблеми з сумісністю.

$ pip show requests
Name: requests
Version: 2.32.3
Summary: Python HTTP for Humans.
Home-page: https://requests.readthedocs.io
Author: Kenneth Reitz
Author-email: me@kennethreitz.org
License: Apache-2.0
Location: C:\Users\Nazar\OneDrive\Документы\GitHub\2024_kn240-oop\Lib\site-packages
Requires: certifi, charset-normalizer, idna, urllib3
Required-by:

$ pip install requests==2.1
Collecting requests==2.1
  Using cached requests-2.1.0-py2.py3-none-any.whl.metadata (30 kB)
Using cached requests-2.1.0-py2.py3-none-any.whl (445 kB)
Installing collected packages: requests
  Attempting uninstall: requests
    Found existing installation: requests 2.32.3
    Uninstalling requests-2.32.3:
      Successfully uninstalled requests-2.32.3
Successfully installed requests-2.1.0

[notice] A new release of pip is available: 24.3.1 -> 25.0.1
[notice] To update, run: python.exe -m pip install --upgrade pip

$ pip show requests
Name: requests
Version: 2.1.0
Summary: Python HTTP for Humans.
Home-page: http://python-requests.org
Author: Kenneth Reitz
Author-email: me@kennethreitz.com
License: Copyright 2013 Kenneth Reitz
Location: C:\Users\Nazar\OneDrive\Документы\GitHub\2024_kn240-oop\Lib\site-packages
Requires: 
Required-by: 

$ pip uninstall requests
Found existing installation: requests 2.1.0
Uninstalling requests-2.1.0:
  Would remove:
    C:\Users\Nazar\OneDrive\Документы\GitHub\2024_kn240-oop\Lib\site-packages\requests-2.1.0.dist-info\*
    C:\Users\Nazar\OneDrive\Документы\GitHub\2024_kn240-oop\Lib\site-packages\requests\*
Proceed (Y/n)? y
  Successfully uninstalled requests-2.1.0



## Робота з альтернативними бібліотеками: `jikanpy`

**Встановлення:**
```bash
pip install jikanpy-v4
```

**Запуск простого Flask-сервера**:
```bash
* Running on http://127.0.0.1:5000
```
(Результат представлено на скріншоті `anime.png`.)


## Робота з віртуальними середовищами (venv)

### Створення і активація середовища

```bash
python -m venv my_env
source my_env/Scripts/activate
pip install requests
deactivate
```

Перевірка встановлення бібліотеки в середовищі:
```bash
pip show requests
```

### Ігнорування середовища в git

У `.gitignore` додано:
```
my_env/
```

## Робота з Pipenv

**Встановлення:**
```bash
pip install pipenv
```

**Створення середовища:**
```bash
pipenv --python 3.10
```

**Інсталяція бібліотеки:**
```bash
pipenv install requests
```

**Файли, що створюються:**
- `Pipfile`
- `Pipfile.lock`

### Запуск Python-програми через Pipenv

```bash
pipenv run python test.py
```

Приклад коду (`test.py`):
```python
import requests

response = requests.get('https://httpbin.org/')
for line in response.iter_lines():
    print(line)
```

## Робота зі змінними середовища

Файл `.env`:
```
API_KEY=your_api_key
DEBUG=True
```

Pipenv автоматично підвантажує змінні середовища у проєкт.


# Висновки

У ході лабораторної роботи я:

- Ознайомився з поняттям віртуальних середовищ у Python;
- Навчився встановлювати та використовувати сторонні бібліотеки;
- Освоїв інструменти `pip` та `pipenv` для керування залежностями;
- Створив приклади роботи з бібліотеками `requests` та `pyfiglet`;
- Ознайомився з організацією середовищ для розробки із застосуванням `.gitignore` та `.env` файлів.

Ізоляція середовищ дозволяє працювати над декількома проектами одночасно без конфліктів між залежностями, що є важливою практикою у сучасній розробці програмного забезпечення.



