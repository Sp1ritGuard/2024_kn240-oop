import requests
r = requests.get('https://google.com')
print (f"Повернув статус:{r.status_code}")