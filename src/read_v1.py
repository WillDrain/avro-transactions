import sys
from fastavro import reader

print("id,event_time,user_email,amount")

with open(sys.argv[1], "rb") as f:
    for rec in reader(f):
        print(f"{rec['id']},{rec['event_time']},{rec['user_email']},{rec['amount']}")
