import urllib.request
import json

cidade_id = "6324214"
token = "0b3ce2daa36248621c390dfe8ef6750a"
url = f'https://api.openweathermap.org/data/2.5/weather?id={cidade_id}&appid={token}'

resposta = urllib.request.urlopen(url)

#api respondeu um json
string_json = resposta.read()

dicionario = json.loads(string_json)

print(string_json)
print(dicionario)