import requests

def assignment():
    data = {"username": "admin", "password": "123456"}
    response = requests.post(url='http://192.168.60.132:8080/admin/login',json=data)

    text_body = response.text
    print(type(text_body))
    print(text_body)

    json_body = response.json()
    print(type(json_body))
    print(json_body)

    assert 200 == response.status_code
    assert '成功' in json_body['message']
    assert 200 == json_body['code']

    data_dict = json_body['data']
    token_head = data_dict['tokenHead']
    token_ = data_dict['token']
    head = {'Authorization': token_head + ' ' + token_}
    get_info = requests.get(url='http://192.168.60.132:8080/admin/info', headers=head)
    print(get_info.text)
    info_json = get_info.json()

    assert 200 == get_info.status_code
    assert '成功' in info_json['message']
    assert 200 == info_json['code']

    request_get = requests.get('http://192.168.60.132:8080/brand/list?pageNum=1&pageSize=10',headers=head)
    param = {'pageNum':1,'pageSize':3}
    get = requests.get('http://192.168.60.132:8080/brand/list',headers=head)
    print(get.text)
    json=get.json()
    json_data_=json['data']
    list_ = json_data_['list']
    for i in list_:
        print(i)

if __name__ == '__main__':
    pass
