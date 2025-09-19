import requests

from config import token
headers = {"Authorization": f"token {token}"}

def fetchActivity():
    print("Enter name or profile URL:")
    n = input().split("/")
    response = (requests.get(f"https://api.github.com/users/{n[-1]}"))
    if response.status_code != 200:
        print("Wrong name or URL.")
        return 0
    data = (requests.get(f"https://api.github.com/users/{n[-1]}/events")).json()
    if len(data) == 0:
        print("No events found.")
        return 0
    print(f"Overall found {len(data)} events.\n")
    for key in data:
        print(f"Operation {key["type"][:-5]} was made with repo {key["repo"]["name"]} at {key["created_at"][0:10]} {key["created_at"][11:-1]}\n")

fetchActivity()