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
