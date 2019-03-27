
import requests


if __name__ == '__main__':
    login_data = {"username":"admin","password":"123456"}
    login_resp = requests.post(url='http://192.168.60.132:8080/admin/login',json=login_data)
    #要把请求数据的响应拉出来,后面方法的结果(响应数据)存到变量login_response中即可
    print(type(login_resp))
    login_resp_text = login_resp.text
    print(login_resp_text)

    login_resp_json = login_resp.json()
    print(login_resp_json['message'])
