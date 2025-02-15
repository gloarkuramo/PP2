from datetime import datetime, timedelta

today=datetime.now()

filtered=today.replace(microsecond=0)

print(filtered)