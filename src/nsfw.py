import requests
import json
import urllib.request
import xmltodict
from random import randint
from pybooru import Danbooru

class boobs:
    def GetSomeBoobs():
        r = requests.get('http://api.oboobs.ru/boobs/1/1/random')
        data = json.loads(r.content)
        for i in data:
            model = i['model']
            url = 'http://media.oboobs.ru/'+i['preview']
        if model == '':
            model = 'None'
        return model, url



class butts:
    def GetSomeButts():
        r = requests.get('http://api.obutts.ru/butts/1/1/random')
        data = json.loads(r.content)
        for i in data:
            url = 'http://media.obutts.ru/'+i['preview']
        return url

class Rule34:
    def GetSomeRule34(search):
            search = search.replace(' ','&')
            file = urllib.request.urlopen('https://rule34.xxx/index.php?page=dapi&s=post&q=index&tags='+search)
            data = file.read()
            file.close()

            data = xmltodict.parse(data)
            check = None
            if data['posts']['@count'] == '0':
                url = ''
                check = False
                return check, url
            try:
                length = len(data['posts']['post'])
                url = 'http:'+data['posts']['post'][randint(0,length)]['@file_url']
                check = True
                return check, url
            except IndexError:
                check = False
                url = ''
                return check, url
class Booru:
    def GetSomeDanbooruImage(search):
        search = search.replace(' ','_')
        check = None
        client = Danbooru('danbooru')
        try:
            posts = client.post_list(tags=search, limit=18)
            url = str('http://danbooru.donmai.us'+posts[randint(0,len(posts))]['file_url'])
            check = True
            return check, url
        except IndexError:
            url = ''
            check = False
            return check, url
