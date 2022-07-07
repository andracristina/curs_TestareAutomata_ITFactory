# 18. Functie care sa afiseze data si ora curenta din ro
# (bonus: afisati si data si ora curenta din China)
import time
from datetime import datetime

import pytz

now = datetime.now()

print(now)

t = time.localtime()
print(t)


