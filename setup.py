import sys
import json
from operator import eq
import time
import datetime
from json import load
from pybit import usdt_perpetual
from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/processUserInfo/<string:userInfo>', methods=['POST'])
def processUserInfo(userInfo):
    userInfo = json.loads(userInfo)
    print()
    print('USER INFO RECEIVED')
    print(f"User Name: {userInfo['name']}")
    print(f"User Name: {userInfo['type']}")
    
    









x = datetime.datetime(2022, 8, 7)
start = x.timestamp()

#api_key = input("Enter api: ")
#api_secret = input("Enter api: ")
# Collecting data from the API
session_auth = usdt_perpetual.HTTP(
    endpoint="https://api.bybit.com",
    api_key='AFvIthxN9nkD4p4Hcx',
    api_secret='4IsBd8ubFzezPKEGxqVnKc3ZkXvG20LTdNpp'
)


with open('json/walletfund.json', 'w') as js:
    json.dump(session_auth.get_wallet_balance(coin="USDT"), js)
    js.close()
#print(session_auth.wallet_fund_records(coin='USDT'))
with open('json/walletrecordsusdt.json', 'w') as js:
    json.dump(session_auth.wallet_fund_records(coin='USDT',
    start_date='2022-08-04',
    end_date='2022-08-10'), js)
    js.close()
with open('json/walletrecordsbtc.json', 'w') as js:
    json.dump(session_auth.wallet_fund_records(coin='BTC',
    start_date='2022-08-04',
    end_date='2022-08-10'), js)
    js.close()
with open('json/walletrecordsusdt.json', "r") as f:
  data = json.load(f)
  f.close()



for i, x in data.items():
   if i == 'result':
        for k, y in x.items():
            if y == None:
                print("good")
            else:
                for z in y:
                    for v, y in z.items():
                        if (v == 'type'):
                            if(y == 'AccountTransfer'):
                                print('Transfer_detected')
                            
                                
                                
        
closed_pnl_sum = 0
available_balance = 0
equity = 0
walletfund_info = []

infile = open("json/walletfund.json","r")
wallet_content = infile.read()
wallet_closed = json.loads(wallet_content)
wallet = wallet_closed["result"]


for i in wallet:
    walletfund_info.append(wallet["USDT"])
for i in walletfund_info:
    json_object = json.dumps(i)
with open("json/walletBalance.json", "w") as file1:
    file1.write(json_object)
    file1.close()
with open('json/walletBalance.json', "r") as file1:
  data1 = json.load(file1)
  file1.close()
for i, x in data1.items():
    if i == 'equity':
        equity = x
    elif i == 'available_balance':
        available_balance = x

# available balance - (10$ + closed pnl) 
# (equity - startingbalance) * 10

starting_balance = 200
win_percentage = ((equity - starting_balance) / starting_balance) * 100
print("{0:.2f} $".format(equity))
print("PnL: {0:.2f}%".format(win_percentage))


