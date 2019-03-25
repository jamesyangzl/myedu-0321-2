
import requests


if __name__ == '__main__':
    data = {"username": "admin", "password": "123456"}
    response = requests.post(url='http://192.168.60.132:8080/admin/login',json=data)

    text_body = response.text
    print(type(text_body))
    print(text_body)

    json_body = response.json()
    print(type(json_body))
    print(json_body)