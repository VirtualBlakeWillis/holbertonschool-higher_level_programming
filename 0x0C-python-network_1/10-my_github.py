#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""

# https://github.com/VirtualBlakeWillis

if __name__ == "__main__":
    import requests
    from sys import argv

    username = argv[1]
    password = argv[2]
    url = "https://api.github.com/users/{}".format(username)
    req = requests.get(url).json()
    print(req['id'])
