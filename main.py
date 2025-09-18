import requests

token = "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"
headers = {"Authorization": f"token {token}"}

data = (requests.get("https://api.github.com/users/skyvva1k3r"))

data = data.json()

print(data)