from datetime import datetime
import json
import os, requests

def upAvt(username: str, password: str, img: str):
    csrf = requests.get("https://www.instagram.com/accounts/login/").cookies['csrftoken']

    data = {
        'username': username,
        'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:{int(datetime.now().timestamp())}:{str(password)}',
        'queryParams': {},
        'optIntoOneTap': 'false'
    }

    login_header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Safari/537.36",
        "X-Requested-With": "XMLHttpRequest",
        "Referer": "https://www.instagram.com/accounts/login/",
        "x-csrftoken": csrf
    }

    login_response = requests.post("https://www.instagram.com/accounts/login/ajax/", data=data, headers=login_header)
    json_data = json.loads(login_response.text)

    if json_data["authenticated"]:
        cookies = login_response.cookies.get_dict()
        cookie = ""
        for x in cookies:
            cookie += f"{x}={cookies[x]};"
        print("Cookie: {}".format(cookie))
    else:
        print("login failed ", login_response.text)


    # # img = "a.jpg"
    # # cookie = 'csrftoken=jmJ4eK81a0tpl0MstxUXyMgzwqAcIRzx;ds_user_id=54679876756;ig_did=05056291-7B5D-46C3-BEED-F018C5A4978F;mid=YwrVhQAEAAHopskppO4PDeUrZuMR;rur="NAO\05454679876756\0541693190407:01f7e7ba3894c5d23bf184666dea177cb1785869a08ff3d2c492860c0c0d307e0261f732";sessionid=54679876756%3AageMOhmiSx10gu%3A27%3AAYfv-_irUOf-QMTl7THZoJ7f4S2MX_5nusy9Zed_ng;'
    # headers = {
    # "X-CSRFToken": cookies['csrftoken'],
    # "X-Requested-With": "XMLHttpRequest",
    # "Content-Length": str(os.path.getsize(img)),
    # "Cookie": cookie
    # }

    # upAvt = requests.post("https://www.instagram.com/accounts/web_change_profile_picture/", headers=headers, files = {'profile_pic': open(img,'rb') }, data = {"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg", "Content-Type": "image/jpeg"}).json()
    # print(upAvt)












while(True):
    user = input("Username: ")
    if user == "":
        break
    passwd = input("Password: ")
    upAvt(user, passwd, r"C:\Users\admin\Desktop\avt\2.jpg")