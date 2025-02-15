from datetime import datetime

a=datetime.now()
date2 = datetime(2024, 2, 10, 10, 30, 0)
print((a-date2).total_seconds())