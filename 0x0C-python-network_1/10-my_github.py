#!/usr/bin/python3
"""
Write a Python script that takes your GitHub credentials (username and
password) and uses the GitHub API to display your id
"""

# https://github.com/VirtualBlakeWillis

if __name__ == "__main__":
    import requests
    from sys import argv

    u_t = "{}:{}".format(argv[1], argv[2])
    url = "https://api.github.com/users/{}".format(u_t)
    req = requests.get(url).json()
    if 'id' in req.keys():
        print(req['id'])
    else:
        print("None")
