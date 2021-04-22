from iqoptionapi.stable_api import IQ_Option
import time
from datetime import datetime

api=IQ_Option("davidkinyanjui052@gmail.com","Letmein20116199623.")
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