import requests

url = "https://api.github.com/search/repositories"
params = {
    "q": "html",
}

response = requests.get(url, params=params)

print(f"Статус код: {response.status_code}")

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Произошла ошибка при запросе.")
