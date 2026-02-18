import json, sys
from fastavro import reader

def load_schema(path):
    with open(path) as f:
        return json.load(f)

reader_schema = load_schema("schemas/transactions_reader.avsc")

print("id,event_time,total_amount,user_email,currency")

with open(sys.argv[1], "rb") as f:
    for rec in reader(f, reader_schema=reader_schema):
        print(
            f"{rec['id']},"
            f"{rec['event_time']},"
            f"{rec['total_amount']},"
            f"{rec['user_email']},"
            f"{rec['currency']}"
        )
