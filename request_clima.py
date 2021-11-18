import urllib.request

cidade_id = "6324214"
token = "0b3ce2daa36248621c390dfe8ef6750a"
url = f'https://api.openweathermap.org/data/2.5/weather?id={cidade_id}&appid={token}'

resposta = urllib.request.urlopen(url)

print(resposta.read()["wind"])

