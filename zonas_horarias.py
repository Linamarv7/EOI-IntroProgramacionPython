#Zonas horarias
from datetime import datetime
from pytz import timezone
import pytz
print(datetime.now(pytz.timezone('Asia/Tokyo')))
print(datetime.now(pytz.timezone('Europe/Madrid')))
