from codecs import unicode_escape_decode
import string
import requests, json, random, os
from datetime import datetime

class Instagram(object):
    def __init__(self, cookie: str) -> None:
        self.cookie = cookie
        self.xcsrftoken = cookie.split("csrftoken=")[1].split(';')[0]
        try:
            headers = {
                'accept': "*/*",
                'authority': "www.instagram.com",
                'content-type': "application/x-www-form-urlencoded",
                'cookie': self.cookie,
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.xcsrftoken,
            }
            post = requests.get("https://www.instagram.com/", headers=headers).text
            self.idProfile = post.split('''"viewerId":"''')[1].split('"}')[0]
            self.x_instagram_ajax = post.split('''rollout_hash":''')[1].split('",')[0]
            self.appId = post.split('''"appId":"''')[1].split('","')[0]
            self.name = json.loads(unicode_escape_decode(post.split('full_name\\":')[1].split(',\\"')[0])[0])
            self.headersApi = {
                'accept': "*/*",
                'authority': "www.instagram.com",
                'content-type': "application/x-www-form-urlencoded",
                'cookie': self.cookie,
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.xcsrftoken,
                'x-requested-with': "XMLHttpRequest",
                'x-ig-app-id': self.appId,
                'x-instagram-ajax': self.x_instagram_ajax,
            }
        except:
            pass
    
    def getInfoCookie(self) -> string:
        try:
            try:
                id = self.idProfile
                name = self.name
            except:
                self.setValues()
                id = self.idProfile
                name = self.name
            return id, name
        except:
            pass
    def proxyAdd(self, proxy: str):
        self.proxyDict = { 
            "http"  : "http://{}".format(proxy), 
            "https" : "http://{}".format(proxy), 
        }
        

    def followUser(self, id: int, proxy = None) -> bool:
        try:
            if proxy != None:
                postFollow = requests.post(f"https://i.instagram.com/api/v1/web/friendships/{id}/follow/", headers=self.headersApi, proxies=self.proxyDict).json()
            else:
                postFollow = requests.post(f"https://i.instagram.com/api/v1/web/friendships/{id}/follow/", headers=self.headersApi).json()
            if postFollow['result'] == "following" and postFollow['status'] == "ok":
                return True
            else:
                return False
        except:
           return False 

    def likePost(self, id: int, proxy = None) -> bool:
        try:
            if proxy != None:
                postRec = requests.post("https://i.instagram.com/api/v1/web/likes/{}/like/".format(id), headers=self.headersApi, proxies=self.proxyDict).json()
            else:
                postRec = requests.post("https://i.instagram.com/api/v1/web/likes/{}/like/".format(id), headers=self.headersApi).json()
            if postRec['status'] == "ok":
                return True
            else:
                return False
        except:
           return False 

    def commentPost(self,id: int, text: str,proxy = None, *idReply) -> bool:
        try:
            if proxy != None:
                if idReply:
                    postCmt = requests.post(f"https://i.instagram.com/api/v1/web/comments/{id}/add/", data={'comment_text': text, 'replied_to_comment_id': str(idReply[0])}, headers=self.headersApi, proxies=self.proxyDict).json()
                else:
                    postCmt = requests.post(f"https://i.instagram.com/api/v1/web/comments/{id}/add/", data={'comment_text': text, 'replied_to_comment_id': ''}, headers=self.headersApi,proxies=self.proxyDict).json()
            else:
                if idReply:
                    postCmt = requests.post(f"https://i.instagram.com/api/v1/web/comments/{id}/add/", data={'comment_text': text, 'replied_to_comment_id': str(idReply[0])}, headers=self.headersApi).json()
                else:
                    postCmt = requests.post(f"https://i.instagram.com/api/v1/web/comments/{id}/add/", data={'comment_text': text, 'replied_to_comment_id': ''}, headers=self.headersApi).json()
            if postCmt['status'] == "ok" and postCmt['text'] == text:
                return True
            else:
                return False
        except:
            return False
    
    def likeCmt(self, id: int, proxy = None) -> bool:
        try:
            if proxy != None:
                likeCmt = requests.post("https://www.instagram.com/web/comments/like/{}/".format(id), headers=self.headersApi, proxies=self.proxyDict).json()
            else:
                likeCmt = requests.post("https://www.instagram.com/web/comments/like/{}/".format(id), headers=self.headersApi).json()
            if likeCmt['status'] == "ok":
                return True
            else:
                return False
        except:
           return False 
    
    def up_avt(self, img_path: str, proxy = None):
        try:
            headers = {
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
                "accept": "*/*",
                "accept-Language": "en-US,en;q=0.5",
                "accept-Encoding": "gzip, deflate, br",
                "referer": "https://www.instagram.com/",
                'x-csrftoken': self.xcsrftoken,
                'x-requested-with': "XMLHttpRequest",
                'x-ig-app-id': self.appId,
                'x-instagram-ajax': self.x_instagram_ajax,
                "content-length": str(os.path.getsize(img_path)),
                "DNT": "1",
                "x-asbd-id": "198387",
                "connection": "keep-alive",
                "cookie": self.cookie
            }
            if proxy != None:
                upAvt = requests.post("https://i.instagram.com/api/v1/web/accounts/web_change_profile_picture/", files = {'profile_pic': open(img_path,'rb')}, data={"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg","Content-Type": "image/jpeg"}, headers=headers, proxies=self.proxyDict).json()
            else:
                upAvt = requests.post("https://i.instagram.com/api/v1/web/accounts/web_change_profile_picture/", files = {'profile_pic': open(img_path,'rb')}, data={"Content-Disposition": "form-data", "name": "profile_pic", "filename":"profilepic.jpg","Content-Type": "image/jpeg"}, headers=headers).json()
            if upAvt['changed_profile'] == True:
                return True
            else:
                return False
        except Exception as e:
            return False
    
    def up_load_post(self, img_path: str, *caption, proxy = None) -> bool:
        if caption:
            caption = caption[0]
        print(img_path, caption, proxy)
        try:
            upload_id = int(datetime.now().timestamp())
            url_load_img = "https://i.instagram.com/rupload_igphoto/fb_uploader_{}".format(upload_id)
            headers = {
                'content-type': "image/jpeg",
                'cookie': self.cookie,
                'offset': "0",
                'user-agent': f"Mozilla/5.0 (Windows NT {random.choice(['7', '8', '10', '11'])}.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(90, 104)}.0.0.0 Safari/537.36",
                'x-csrftoken': self.xcsrftoken,
                'x-requested-with': "XMLHttpRequest",
                'x-entity-length': str(os.path.getsize(img_path)),
                'x-entity-name': "fb_uploader_{}".format(upload_id),
                'x-ig-app-id': self.appId,
                'x-instagram-ajax': self.x_instagram_ajax,
                'x-instagram-rupload-params': f'{{"media_type":1,"upload_id":"{upload_id}","upload_media_height":780,"upload_media_width":780}}',
            }
            dataPost = open(img_path, "rb")
            url_up_post = "https://i.instagram.com/api/v1/media/configure/"
            data = {
                'source_type': "library",
                'caption': str(caption) if caption else "",
                'upload_id': upload_id,
                'disable_comments': "0",
                'like_and_view_counts_disabled': "0",
                'igtv_share_preview_to_feed': "1",
                'is_unified_video': "1",
                'video_subtitles_enabled': "0"
            }
            if proxy != None:
                print(self.proxyDict)
                print(requests.post(url=url_load_img,data=dataPost, headers=headers, proxies=self.proxyDict).json())
                up_post = requests.post(url = url_up_post, headers = self.headersApi, data = data, proxies=self.proxyDict).json()
            else:
                print(requests.post(url=url_load_img,data=dataPost, headers=headers).json())
                up_post = requests.post(url = url_up_post, headers = self.headersApi, data = data).json()
            print(up_post)
            if up_post['status'] == "ok":
                return True
            else:
                return False
        except Exception as e:
            return False

# ig = Instagram('rur="EAG\05455965676825\0541696950444:01f7b9cbf9e81bc20b93d853fc799920d582a6c15ec061e780df78628e7fbb9fe3743957";datr=HjVEYzqSTEIRQzKSHfKbQskk;mid=Y0Q08gAEAAGD3XUWmOxVUWtP-HUU;csrftoken=FNQExe5YF0o18gQqyhYTojm6gvbgr4LO;ig_nrcb=1;sessionid=55965676825%3A858nNLIxnQRV8n%3A29%3AAYeoMI_p4yi4FphYRsgL3fkp4dHbRjRRrIWOBBfm6w;ds_user_id=55965676825;ig_did=F2814E22-E075-4097-AFCA-BFA1A3AB2130;')
# ig.proxyAdd('116.104.246.132:44169')
# print(ig.up_load_post('K:/Desktop/avt/78120482_284916806219213_3180643575855579136_n.jpg', "Auto By Tài", proxy = True))
