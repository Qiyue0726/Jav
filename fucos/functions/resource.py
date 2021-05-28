import requests
from bs4 import BeautifulSoup

from fucos.models import FocusActor, SysOptions

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66"}



def getVideos():
    videoList = []
    javUrl = SysOptions.objects.get(option_key='domain').option_value
    actors = FocusActor.objects.all()
    showNum = int(SysOptions.objects.get(option_key='showNum').option_value)
    for actor in actors:
        resp = requests.get(javUrl + "/vl_star.php?s="+actor.actor_id, headers=headers)
        soup = BeautifulSoup(resp.text, features="lxml")
        videos = soup.findAll("div", attrs={"class":"video"})

        list = []
        for v in videos[0:showNum]:
            video = {
                "id": v['id'][4:],
                "href": "http://www.f50q.com/cn" + v.a['href'][1:],
                "code": v.div.string,
                "cover": "http:" + v.img['src'],
                "imgHeight": v.img['height'],
                "imgWidth": v.img['width'],
                "title": v.find("div", attrs={"class":"title"}).string,
            }
            list.append(video)

        videoList.append({
            "actorId":actor.actor_id,
            "actorName":actor.name,
            "videos":list
        })

    return videoList

