import requests


#url='https://www.infomoney.com.br'
#resposta=requests.get(url)
#print(url)
#print(resposta)
#print(resposta.text)
#print(resposta.headers)


#using json
url='https://jsonplaceholder.typicode.com/posts/1'
response=requests.get(url)
data =response.json()
print(data)