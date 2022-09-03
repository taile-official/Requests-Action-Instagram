# Requests-Action-Instagram

Project Requests instagram using Python code

<p align="center">
<a href="#"><img alt="Forks" src="https://img.shields.io/github/forks/taile-official/Requests-Action-Instagram?style=for-the-badge"></a>
<a href="#"><img alt="last commit (main)" src="https://img.shields.io/github/last-commit/taile-official/Requests-Action-Instagram/main?color=green&style=for-the-badge"></a>
<a href="#"><img alt="Repo stars" src="https://img.shields.io/github/stars/taile-official/Requests-Action-Instagram?style=for-the-badge&color=yellow"></a>
<a href="https://github.com/taile-official/Requests-Action-Instagrams"><img alt="MatrixTM issues" src="https://img.shields.io/github/issues/taile-official/Requests-Action-Instagram?color=purple&style=for-the-badge"></a>

  

## Downloads - Tải Xuống

You can download it from [GitHub Project](https://github.com/taile-official/Requests-Action-Instagram)

### Getting Started

**Requirements**

* [dnspython](https://github.com/rthalley/dnspython)
* [cfscrape](https://github.com/Anorov/cloudflare-scrape)
* [impacket](https://github.com/SecureAuthCorp/impacket)
* [requests](https://github.com/psf/requests)
* [Python3](https://www.python.org/downloads/release/python-3106/)
* [PyRoxy](https://github.com/MatrixTM/PyRoxy)
* [icmplib](https://github.com/ValentinBELYN/icmplib)
* [certifi](https://github.com/certifi/python-certifi)
* [psutil](https://github.com/giampaolo/psutil)
* [yarl](https://github.com/aio-libs/yarl)
---

**Channel**
* YouTube : https://www.youtube.com/TaiLeOfficial

## Documentation
**Clone and Install Script**

```shell script
git clone https://github.com/taile-official/Requests-Action-Instagram
cd Requests-Action-Instagram
pip install -r thuvien.txt
```


**Import**

```shell script
import Instagram
```

### OR

```shell script
from InstagramApi import Instagram
```

**Gọi Class**

```shell script
cookie = "Cookie Web Instagram"
ins = Instagram(cookie)
```
Gọi class Instagram với tham số là cookie web Instagram ``` ins = Instagram(cookie)```
Những lần tiếp theo chỉ cần gọi hàm theo ý vì cookie đã được đính vào class

## Định cấu hình, Info Cookie
**Sau khi gọi class Instagram với cookie**
```shell script
 ins.setValues()
```
Dùng để set các tường name trong cookie tổng để URL trả về kết quả chính xác
Nếu không gọi hàm này sẽ ko thể sử dụng các hàm khác

  
## Get Info - Lấy thông tin cá nhân
```shell script
infoUser = ins.getInfo()
print(infoUser)
#(5472148373, "Lê Tuấn Tài")
```
  
## Follow - Theo dõi by ID
```shell script
follow = ins.followId(id user instagram)
print(follow) # => bool : True or False

'''
follow = ins.followId(54636757344)
print(follow)
>>> True
'''
```

## Like Post - Theo dõi by ID
```shell script
like = ins.likePost(id post instagram)
print(like) # => bool : True or False

'''
like = ins.likePost(72636374624757344)
print(like)
>>> True
'''
```

## Comment Post - Comment by ID POST
```shell script
cmt = ins.commentPost(id post instagram)
print(cmt) # => bool : True or False

'''
cmt = ins.commentPost(72636374624757344)
print(cmt)
>>> True
'''
```

## Reply Comment Post - Reply Comment by ID POST
```shell script
cmt = ins.commentPost(id post instagram, id cmt)
print(cmt) # => bool : True or False

'''
cmt = ins.commentPost(72636374624757344, 548236722)
print(cmt)
>>> True
'''
```
