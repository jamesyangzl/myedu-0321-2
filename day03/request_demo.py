
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

    # assert 200 == response.status_code
    # assert '成功' in json_body['message']
    # assert 200 == json_body['code']

    data_dict = json_body['data']
    token_head = data_dict['tokenHead']
    token_ = data_dict['token']
    head = {'Authorization': token_head+''+token_}

    get_info = requests.get(url='http://192.168.60.132:8080/admin/info',headers=head)
    print(get_info.text)


