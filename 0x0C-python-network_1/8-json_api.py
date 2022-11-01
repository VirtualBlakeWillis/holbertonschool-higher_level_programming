#!/usr/bin/python3
"""
Write a Python script that takes in a letter and sends a POST request
to http://0.0.0.0:5000/search_user with the letter as a parameter.
"""

if __name__ == "__main__":
    import requests
    from sys import argv
    if len(argv) >= 2:
        q = argv[1]
    else:
        q = ""
    data = {'q': q}
    req = requests.post('http://0.0.0.0:5000/search_user', data).json()

    if len(req):
        print("[{}] {}".format(req['id'], req['name']))
    else:
        print("No result")
