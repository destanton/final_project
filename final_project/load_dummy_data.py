import requests

url = "https://randomuser.me/api/?nat=us&results=100"
results = requests.get(url).json()
print(results["results"][1])
