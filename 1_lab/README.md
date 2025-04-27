##


```bash
cd 1_lab
ls -la
mkdir venv_env
cd venv_env
python -m venv .my_env
#source .my_env/bin/activate
source .my_env/scripts/activate # Для Windows
pip install requests
pip list
python 1.py

pip freeze > requirements.txt
deactivate
# Видаляємо папку віртуального середовища .my_env
python -m venv .my_env
source .my_env/bin/activate
pip install -r requirements.txt
python 1.py
deactivate
```
##
```bash
pip install pipenv
pipenv -h
cd pipenv_env/
pipenv --python 3.12
pipenv install flake8 --dev
pipenv install requesta
pipenv install

pipenv run python 1.py
pipenv run flake8 .
