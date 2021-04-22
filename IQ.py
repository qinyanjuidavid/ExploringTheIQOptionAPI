from iqoptionapi.stable_api import IQ_Option
import time
from datetime import datetime
api=IQ_Option("davidkinyanjui052@gmail.com","Letmein20116199623.")
api.connect()
api.start_candles_stream("EURUSD",1,2)
candle=api.get_realtime_candles("EURUSD",1)
print(candle)