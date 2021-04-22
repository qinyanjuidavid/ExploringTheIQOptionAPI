from iqoptionapi.stable_api import IQ_Option
import time
from datetime import datetime

api=IQ_Option("email","password")
api.connect()
print(api)
goal="EURUSD"
size=1
maxdict=1

print("Start stream...")
api.start_candles_stream(goal, size, maxdict)
print("Print candles...")
candle = api.get_realtime_candles(goal, size)
key = list(candle)[0]
current_price = candle[key]['close']
print("Current price", current_price)

duration=1
amount=1
buy="call"
#api.subscribe_strike_list(goal)
data=api.get_realtime_strike_list(goal,duration)
price_list=list(data.keys())
close_current_price=[]
for p_list in price_list:
    close_current_price.append(abs(current_price-float(p_list)))
most_close_price=price_list[close_current_price.index(min(close_current_price))]
print("Most close price: {}\nCurrent price: {}".format(most_close_price,current_price))
print(data[str(most_close_price)])


instrument_id=data[choose_price[buy]["id"]]
profit=data[choose_price][buy]["profit"]
print("Choose you want to buy")
print("price:",choose_price,"side:call","instrument_id:",instrument_id,"profit:",profit)

#put instrument id to buy
buy_check,id=api.buy_digital(amount,instrument_id)
if buy_check:
    print("wait for check win")
    #Check win
    while True:
        check_close,win_money=api.check_win_digital(id)
        if check_close:
            if float(win_money)>0:
                win_money=("%.2f" %(win_money))
                print("You win",win_money,"money")
            else:
                print("you loose")
            break
    api.unsubscribe_strike_list(buy)
else:
    print("Fail to buy, Please run again, digit i")