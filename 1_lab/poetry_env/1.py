import requests
import os

r = requests.get('https://google.com')
if r.status_code == 200:
    print(r.content)
else:
    print("Код не готовий до продакшину")
