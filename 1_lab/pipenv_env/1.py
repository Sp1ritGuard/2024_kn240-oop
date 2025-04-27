import requests
import os

print(os.environ.get("VERSION"))
if os.environ.get("stage") == "prod":
    r = requests.get('https://google.com')
    print(r.status_code)
else:
    print("Код не готовий до продакшину")
