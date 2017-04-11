import urllib.request
import xmltodict
from random import randint

class Cat:
    def GetSomeRandomKitty():
        image_type = ['gif','jpg','png']
        file = urllib.request.urlopen('http://thecatapi.com/api/images/get?format=xml&type='+image_type[randint(0,2)]+'&results_per_page=1')
        data = file.read()
        file.close()

        data = xmltodict.parse(data)
        kitty = data['response']['data']['images']['image']['url']
        return kitty
