import datetime
x=datetime.datetime.now()
yesterday=x+datetime.timedelta(-1)
today=x
tommorow=x+datetime.timedelta(1)
print(yesterday,today,tommorow,sep="\n")