import sys
import json
from operator import eq
import time
import datetime
from json import load
from pybit import usdt_perpetual
from flask import Flask, render_template

FinalOutput = [];

data = []
x = datetime.datetime(2022, 11, 18)
start = x.timestamp()
count = 0;
count2 = 0;
count3 = 0;
count4 = 0;
#api_key = input("Enter api: ")
#api_secret = input("Enter api: ")
# Collecting data from the API

session_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='SPZPIREXRBJEKLZEYJ',
    api_secret='QWISBCWGGHSOSNSRHBHDEZEZZYABBUTDJCNL'
)
session_auth2 = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='SPZPIREXRBJEKLZEYJ',
    api_secret='QWISBCWGGHSOSNSRHBHDEZEZZYABBUTDJCNL'
)
session_auth3 = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='SPZPIREXRBJEKLZEYJ',
    api_secret='QWISBCWGGHSOSNSRHBHDEZEZZYABBUTDJCNL'
)
session_auth4 = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='SPZPIREXRBJEKLZEYJ',
    api_secret='QWISBCWGGHSOSNSRHBHDEZEZZYABBUTDJCNL'
)
session_auth5 = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='SPZPIREXRBJEKLZEYJ',
    api_secret='QWISBCWGGHSOSNSRHBHDEZEZZYABBUTDJCNL'
)
session_auth_dict = [session_auth, session_auth2,session_auth3,session_auth4,session_auth5]
for i in session_auth_dict:
    
    with open('json/walletfund{count}.json'.format(count = count), 'w') as js:
        json.dump(i.get_wallet_balance(coin="USDT"), js)
        js.close()
    count += 1;    
#print(session_auth.wallet_fund_records(coin='USDT'))
    with open('json/walletrecordsusdt{count}.json'.format(count = count), 'w') as js:
        json.dump(i.wallet_fund_records(coin='USDT',
        start_date='2022-11-18',
        end_date='2022-11-20'), js)
        js.close()
    with open('json/walletrecordsbtc{count}.json'.format(count = count), 'w') as js:
        json.dump(i.wallet_fund_records(coin='BTC',
        start_date='2022-11-18',
        end_date='2022-11-20'), js)
        js.close()
    with open('json/walletrecordsusdt{count}.json'.format(count = count), "r") as f:
        data.append(json.load(f))
        f.close()


for v in data:
    print(v)
    for i, x in v.items():
        if i == 'result':
            for k, y in x.items():
                if y == None:
                    FinalOutput.append("No transfer detected");
                else:
                    for z in y:
                        for v, y in z.items():
                            if (v == 'type'):
                                if(y == 'ExchangeOrderDeposit'):
                                    FinalOutput.append("Transfer Detected");

   
    
                            
                                
                                
        
closed_pnl_sum = []
available_balance = []
equity = []
walletfund_infoList = []
walletfund_info = []
win_percentage = []
for v in session_auth_dict:  # za vsichki APIta
    infile = open("json/walletfund{count}.json".format(count = count2),"r")  #otvarqme funda
    wallet_content = infile.read()
    wallet_closed = json.loads(wallet_content)
    wallet = wallet_closed["result"]  #vzimame resulta
    
    

    for i in wallet:    # ot rezulta tursim USDT balanca
        walletfund_info.append(wallet["USDT"])
    for i in walletfund_info:
        json_object = json.dumps(i)
    with open("json/walletBalance{count}.json".format(count = count2), "w") as file1:
        file1.write(json_object)
        file1.close()
    with open('json/walletBalance{count}.json'.format(count = count2), "r") as file1:
        data1 = json.load(file1)
        file1.close()
    for i, x in data1.items():
        if i == 'equity':
            equity.append(x);
        elif i == 'available_balance':
            available_balance.append(x)
    count2+=1;
# available balance - (10$ + closed pnl) 
# (equity - startingbalance) * 10

starting_balance = [10, 20, 30 ,40 ,50]
for v in session_auth_dict:
    
    win_percentage.append(((equity[count3] - starting_balance[count3]) / starting_balance[count3]) * 100)
    # print("User{count3} {0:.2f} $".format(equity[count3], count3 = count3+1) + " PnL: {0:.2f}%".format(win_percentage[count3]))
    FinalOutput[count3] += " User{count3} {0:.2f} $".format(equity[count3], count3 = count3+1) + " PnL: {0:.2f}%".format(win_percentage[count3])
    
    count3+=1;
for i in FinalOutput:
    print(i)
