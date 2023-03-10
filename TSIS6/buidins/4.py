import time
number=int(input())
timed=int(input())
time.sleep(timed/1000.0000)
print(f"Square root of {number} after {timed} miliseconds is {number**0.5}")