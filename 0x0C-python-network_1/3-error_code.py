#!/usr/bin/python3
"""
Write a Python script that takes in a URL, sends a request
to the URL and displays the body of the response (decoded in utf-8).
"""

if __name__ == "__main__":
    import urllib.request
    from urllib.error import URLError
    from sys import argv

    url = argv[1]
    try:
        with urllib.request.urlopen(url) as response:
            html = response.read()
            print(html.decode('utf-8'))
    except URLError as e:
        print("Error Code: {}".format(e.code))
