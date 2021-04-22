from iqoptionapi.stable_api import IQ_Option
import time
from datetime import datetime

api=IQ_Option("davidkinyanjui052@gmail.com","Letmein20116199623.")
api.connect()
print(api)
goal="EURUSD"
size=1
maxdict=1