from xml.dom.minidom import ReadOnlySequentialNamedNodeMap
import requests
import json

url = "https://weather.contrateumdev.com.br/api/weather/city/"


c = input('Qual a cidade? ')
e = input('Qual o estado? ')

querystring = {"city":"{},{}".format(c,e)}
#querystring = {"city":"maceio, alagoas"}

payload = ""

response = requests.request("GET", url, data=payload, params=querystring)

a1 = response.json()
a2 = a1['weather'][0]

temx = a1['main']['temp_max']
temn = a1['main']['temp_min']
tem = a1['main']['temp']

cli = a2['description']

print('A cidade de {} esta com temperatura {} e clima {}'.format(c,tem,cli))
