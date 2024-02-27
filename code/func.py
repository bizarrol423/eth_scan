import requests
import json

TokenETH = "TOKEN"
email = "EMAIL"
id_table = "IDTABLE"
WEI = 1000000000000000000

def get_eth(AccountUrl: str) -> None:
    url = "https://api.etherscan.io/api?module=account&action=balancemulti"
    url += f"&address={AccountUrl}"
    url += "&tag=latest"
    url += f"&apikey={TokenETH}"
    responce = requests.get(url=url).text
    datas = json.loads(responce)
    return(int(datas["result"][0]["balance"])/WEI)
