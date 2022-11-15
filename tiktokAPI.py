from TikTokApi import TikTokApi

api = TikTokApi()

def getTikTokAPI(tag, vId):
    data = []
    for id in vId:
        vidInfo = api.video(id=f'{id}').info()
        vidInfo.replace("\'","\"")
        vidInfo.replace(True,"True")
        vidInfo.replace(False,"False")
        print(vidInfo)

# video = api.video(id='7164362493689662722')
# print(video)

# for video in api.hashtag(name='indonesia').videos(count=5):
#     print(video)