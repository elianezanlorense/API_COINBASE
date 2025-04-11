import requests
from datetime import datetime
from tinydb import TinyDB

def extract_data_bitcoin():
    url = "https://api.coinbase.com/v2/prices/spot"
    response = requests.get(url)
    data = response.json()
    return data

def transform_data_bitcoin(data):
    value = data["data"]["amount"]
    cryptocoin = data["data"]["base"]
    currency = data["data"]["currency"]
    timestamp = datetime.now().timestamp()

    transform_data = {
        "value": value,
        "cryptcoin": cryptocoin,
        "currency": currency,
        "timestamp": timestamp
    }

    return  transform_data

def save_data_tinydb(data, db_name="bitcoin.json"):
    db = TinyDB(db_name)
    db.insert(data)
    print("Data saved successfully!")

if __name__ == "__main__":
    # Extract data
    dados_json = extract_data_bitcoin()
    data_tranform = transform_data_bitcoin(dados_json)
    save_data_tinydb(data_tranform)