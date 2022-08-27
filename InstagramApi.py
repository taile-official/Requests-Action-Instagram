from codecs import unicode_escape_decode
import random, requests, json

class Instagram(object):
    def __init__(self, cookie: str) -> None:
        self.cookie = cookie
        self.xcsrftoken = cookie.split("csrftoken=")[1].split(';')[0]
    
    def setValues(self):
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
    
    def getInfoCookie(self):
        try:
            id = self.idProfile
            name = self.name
        except:
            self.setValues()
            id = self.idProfile
            name = self.name
        return id, name

    def followUser(self, id: int) -> bool:
        try:
            postFollow = requests.post(f"https://www.instagram.com/web/friendships/{id}/follow/", headers=self.headersApi).json()
            if postFollow['result'] == "following" and postFollow['status'] == "ok":
                return True
            else:
                return False
        except:
           return False 

    def likePost(self, id: int or str) -> bool:
        try:
            postRec = requests.post("https://www.instagram.com/web/likes/{}/like/".format(id), headers=self.headersApi).json()
            if postRec['status'] == "ok":
                return True
            else:
                return False
        except:
           return False 

    def commentPost(self,id: int or str, text: str, *idReply) -> bool:
        try:
            if idReply:
                postCmt = requests.post(f"https://www.instagram.com/web/comments/{id}/add/", data={'comment_text': text, 'replied_to_comment_id': str(idReply[0])}, headers=self.headersApi).json()
            else:
                postCmt = requests.post(f"https://www.instagram.com/web/comments/{id}/add/", data={'comment_text': text, 'replied_to_comment_id': ''}, headers=self.headersApi).json()
            print(postCmt)
            if postCmt['status'] == "ok" and postCmt['text'] == text:
                return True
            else:
                return False
        except:
            return False
    
    def likeCmt(self, id: int or str) -> bool:
        try:
            likeCmt = requests.post("https://www.instagram.com/web/comments/like/{}/".format(id), headers=self.headersApi).json()
            if likeCmt['status'] == "ok":
                return True
            else:
                return False
        except:
           return False 
