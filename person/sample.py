from datetime import datetime

then = datetime.now()
x = input("wait")
now = datetime.now()


difference = now - then
print(difference.days)