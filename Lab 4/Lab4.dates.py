import datetime
from datetime import timedelta
from random import randint

"""x = datetime.datetime.now()
five = timedelta(5)
five_ago = x - five
print(five_ago.strftime("%A"))"""



"""x = datetime.datetime.now()
d = timedelta(1)
tomorrow = x + d
yesterday = x - d
print(x)
print(tomorrow)
print(yesterday)"""



"""x = datetime.datetime.now()
print(x.strftime("%Y-%d-%j %H:%M:%S"))"""


from datetime import datetime
"""def difference(x,y):
    timedelta = x-y
    return abs(timedelta.days*24*3600+timedelta.seconds)
n = randint(1,7)
x = datetime.now()
d = timedelta(n)
y = x + d
print(f"Today: {x}")
print(f"After {n} days: {y}")
print(f"Until {n} day left: {difference(x,y)} seconds")"""



