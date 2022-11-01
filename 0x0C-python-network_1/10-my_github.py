#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""

# https://github.com/VirtualBlakeWillis

if __name__ == "__main__":
    import requests
    from requests.auth import HTTPBasicAuth
    from sys import argv

    username = argv[1]
    password = argv[2]
    url = "https://api.github.com/user"
    req = requests.get(url, auth=HTTPBasicAuth(username, password)).json()
    if 'id' in req.keys():
        print(req['id'])
    else:
        print("None")
