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

#using json and parameters
url='https://jsonplaceholder.typicode.com/comments'
params={'postId':1}
response=requests.get(url,params=params)
comments =response.json()
print(len(comments))



# Returning the bitcoin price by default
url = "https://api.coinbase.com/v2/prices/spot"
headers = {
    "Accept": "application/json",
    "User-Agent": "MinhaAplicacao/1.0"
}
params = {"currency": "USD"}  # Currency

response = requests.get(url, headers=headers, params=params)
data = response.json()
print("Bitcoin price (USD):", data["data"]["amount"])

#Updating the crypto

crypto = "ETH"       # You can change this to BTC, SOL, DOGE, etc.
currency = "USD"     # You can also change this to EUR, GBP, etc.

url = f"https://api.coinbase.com/v2/prices/{crypto}-{currency}/spot"
headers = {
    "Accept": "application/json",
    "User-Agent": "MinhaAplicacao/1.0"
}

response = requests.get(url, headers=headers)
data = response.json()

print(f"Price {crypto} ({currency}):", data["data"]["amount"])
