from TikTokApi import TikTokApi


api = TikTokApi()

# video = api.video(id='7164362493689662722').info()
# print(video)

for video in api.hashtag(name='indonesia').videos(count=5):
    print(video)