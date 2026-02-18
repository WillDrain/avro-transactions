import sys
from fastavro import reader

print("id,event_time,total_amount,currency")

with open(sys.argv[1], "rb") as f:
    for rec in reader(f):
        print(f"{rec['id']},{rec['event_time']},{rec['total_amount']},{rec['currency']}")
