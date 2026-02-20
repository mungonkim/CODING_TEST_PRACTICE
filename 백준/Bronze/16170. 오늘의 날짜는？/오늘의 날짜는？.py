from datetime import datetime

now = datetime.utcnow()
print(now.year)
print(now.strftime("%m"))
print(now.strftime("%d"))