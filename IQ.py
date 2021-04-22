from iqoptionapi.stable_api import IQ_Option
import time
from datetime import datetime
api=IQ_Option("email","password")
api.connect()
api.start_candles_stream("EURUSD",1,2)
candle=api.get_realtime_candles("EURUSD",1)
print(candle)

key=list(candle)[0]
current_price=candle[key]['close']
api.change_balance("PRACTICE")
balance=api.get_balance()
print("Balance:",balance)
profit=api.get_all_profit()
#print("Profit:",profit)
real=api.get_all_realtime_candles()
#print("Get all realtime:",real)
#print(api.get_candles("EURUSD",1,111,time.time()))
#Checking for all open markets
#print(api.get_all_open_time())
checkIfOpen=api.get_all_open_time()#Check if the market is open,forex,cfd,crypto,digital,binary,turbo
print(checkIfOpen["digital"]["EURUSD"]["open"])
print(api.get_top_assets_updated("forex"))

while True:
    api.start_candles_stream("EURUSD",1,2)
    candle=api.get_realtime_candles("EURUSD",1)
    key=list(candle)[0]
    current_price=candle[key]['close']
    print("Current Price: {}".format(current_price))
    print(type(current_price))
    if current_price <= 1.4:
        time.sleep(1)
        #c=api.buy(1,"EURUSD","call",1)
        check,order_id=api.buy_order("forex","USDCAD","buy",100,1,"market")
        print("Buying")
        print(api.get_async_order(order_id))
#Still Finding a way to trade the stocks, The current code only works in the binary option"