from datetime import datetime, timedelta

today=datetime.now().date()

past=today-timedelta(days=5)

print(past)