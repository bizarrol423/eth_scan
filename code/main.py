import gspread
import func

if __name__ == "__main__":
    sa = gspread.service_account(filename="YORE_FILE")
    sh = sa.open("eth_scan")
    wks = sh.worksheet("Лист1")
    accounts = wks.get('A1:A999')
    UpdateTable = []
    for account in accounts:
        CountETH = func.get_eth(account[0])
        print(account[0], CountETH)
        UpdateTable.append([CountETH])
    wks.update(range_name = 'B1', values = UpdateTable)
    print("\ncomplete link to you're google table")
    print("YOURE_LINK")