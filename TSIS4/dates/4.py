from datetime import datetime
x=datetime(2020,2,23,12,22,23)
y=datetime(2020,2,2,21,3,23)
z=x-y
print(int(z.total_seconds()))