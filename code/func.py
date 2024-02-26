import requests
import json


WEI = 1000000000000000000

def get_eth(AccountUrl: str, token: str) -> None:
    url = "https://api.etherscan.io/api?module=account&action=balancemulti"
    url += f"&address={AccountUrl}"
    url += "&tag=latest"
    url += f"&apikey={token}"
    responce = requests.get(url=url).text
    data = json.loads(responce)
    for account in data["result"]:
        print(int(account['balance'])/WEI)