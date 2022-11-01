#!/usr/bin/python3
""" Write a Python script that fetches https://intranet.hbtn.io/status """


if __name__ == "__main__":
    from requests import get

    response_obj = get("https://intranet.hbtn.io/status")
    text = response_obj.text
    print("Body response:")
    print("\t- type: {}".format(type(text)))
    print("\t- content: {}".format(text))
