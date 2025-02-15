from datetime import datetime, timedelta

today=datetime.now().date()
day=timedelta(days=1)
print(today-day)
print(today)
print(today+day)
