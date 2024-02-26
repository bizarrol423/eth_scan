import func


if __name__ == "__main__":
    token = ""
    accounts = ["0x00772D39fBa439e1e2453fE0671bC13f81169F61",
                "0x6ba9F6A46B9337db27FfdE13ca98B00Edf4A96a1",
                "0x780e882B20A59f9722fd59fC7B6b1127A0A28A12",
                "0xde0b295669a9fd93d5f28d9ec85e40f4cb697bae"]
    i = 0
    while i< len(accounts):
        if (i+20 > len(accounts)):
            AccountUrl = ",".join(accounts[i:len(accounts)])    
        else:
            AccountUrl = ",".join(accounts[i:i+20])
            i+=20
        print(AccountUrl)
        func.get_eth(AccountUrl, token)
        if (i+20 > len(accounts)):
            break
        