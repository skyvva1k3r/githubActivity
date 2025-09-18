import requests

from config import token
headers = {"Authorization": f"token {token}"}

print(requests.get("https://api.github.com/users/tafia/events"))