import requests
from bs4 import BeautifulSoup

from focus.models import Actor, SysOptions

headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36 Edg/90.0.818.66"}
javUrl = SysOptions.objects.get(option_key='domain').option_value

def getActor():

    codes = list(map(chr, range(65, 91)))
    # codes = ['L',"X"]
    for code in codes:
        actors=[]
        url = javUrl + "/star_list.php?prefix="+code
        page = 0

        ## 获取该字母相关的page数量
        try:
            resp = requests.get(url,headers=headers)
            soup = BeautifulSoup(resp.text, features="lxml")
            # if soup.find('div', attrs={'class':'starbox'}) is not None:
            if len(soup.find('div', attrs={'class':'page_selector'}).text) != 0:
                page = int(soup.find('a', attrs={'class':'page last'})['href'][32:])
            else:
                page = 1
            # else:
            #     print('字母 %s 没有数据'% code)
            #     continue
        except:
            print("字母 %s 解析出错，url：%s" % (code, url))

        if page > 0:
            for p in list(range(1,page+1)):
                boxUrl = javUrl+"/star_list.php?prefix="+code+'&page='+p.__str__()
                ## 解析女优信息并入库
                try:
                    boxResp = requests.get(boxUrl, headers=headers)
                    boxSoup = BeautifulSoup(boxResp.text, features="lxml")
                    stars = boxSoup.findAll('div', attrs={'class':'searchitem'})
                    for star in stars:
                        actors.append(Actor(actor_id=star['id'], actor_name=star.find('a').string, letter=code))
                    Actor.objects.bulk_create(actors)
                except:
                    print("字母 %s：第 %d 页解析出错,url: %s" % (code,p, boxUrl))
                actors.clear()


def increActor(letter,page):
    boxUrl = javUrl+"/star_list.php?prefix="+letter+'&page='+page.__str__()
    actors=[]
    ## 解析女优信息并入库
    try:
        boxResp = requests.get(boxUrl, headers=headers)
        boxSoup = BeautifulSoup(boxResp.text, features="lxml")
        stars = boxSoup.findAll('div', attrs={'class':'searchitem'})

        for star in stars:
            actors.append(Actor(actor_id=star['id'], actor_name=star.find('a').string, letter=letter))
        Actor.objects.bulk_create(actors)
    except:
        print("字母 %s: 第 %d 页解析出错,url: %s" % (letter,page, boxUrl))
    actors.clear()

def flash():
    letters = list(map(chr, range(65, 91)))
    # letters = ['L',"X"]
    for letter in letters:
        newActors = []
        url = javUrl + "/star_list.php?prefix="+letter
        page = 0

        ## 获取该字母相关的page数量
        try:
            resp = requests.get(url,headers=headers)
            soup = BeautifulSoup(resp.text, features="lxml")
            # if soup.find('div', attrs={'class':'starbox'}) is not None:
            if len(soup.find('div', attrs={'class':'page_selector'}).text) != 0:
                page = int(soup.find('a', attrs={'class':'page last'})['href'][32:])
            else:
                page = 1
            # else:
            #     print('字母 %s 没有数据'% code)
            #     continue
        except:
            print("字母 %s 解析出错，url：%s" % (letter, url))

        actors = list(Actor.objects.filter(letter=letter).values_list('actor_id',flat=True))

        if page > 0:
            for p in list(range(1,page+1)):
                boxUrl = javUrl+"/star_list.php?prefix="+letter+'&page='+p.__str__()
                ## 解析女优信息并入库
                try:
                    print("获取 %s 第 %d 页成功，开始解析" % (letter,p))
                    boxResp = requests.get(boxUrl, headers=headers)
                    boxSoup = BeautifulSoup(boxResp.text, features="lxml")
                    stars = boxSoup.findAll('div', attrs={'class':'searchitem'})
                    for star in stars:
                        if (star['id'] not in actors):
                            newActors.append(Actor(actor_id=star['id'], actor_name=star.find('a').string, letter=letter))
                    if newActors.__len__() > 0:
                        print(newActors)
                        Actor.objects.bulk_create(newActors) 
                        newActors.clear()
                except:
                    print("字母 %s：第 %d 页解析出错,url: %s" % (letter,p, boxUrl))
            
        actors.clear()
