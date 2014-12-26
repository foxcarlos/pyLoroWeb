#Instalar Dependencias
'''
aptitude install python-simplejson
aptitude install python-httplib2
aptitude install python-six

pip install python-instagram
'''


from instagram.client import InstagramAPI

access_token = "104740353.689a9b6.abc540ee313849eb84992578a08fee0f"
api = InstagramAPI(access_token=access_token)
recent_media, next_ = api.user_recent_media(user_id="689a9b6752e74f01afe8242ccbcd03bc", count=10)
for media in recent_media:
   print(media.caption.text)
