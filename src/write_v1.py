import csv, json, sys
from fastavro import writer, parse_schema

def load_schema(path):
    with open(path) as f:
        return json.load(f)

csv_path = sys.argv[1]
avro_path = sys.argv[2]

schema = parse_schema(load_schema("schemas/transactions_v1.avsc"))

records = []
with open(csv_path) as f:
    reader_csv = csv.DictReader(f)
    for row in reader_csv:
        records.append({
            "id": int(row["id"]),
            "event_time": row["event_time"],
            "user_email": row["user_email"],
            "amount": float(row["amount"])
        })

with open(avro_path, "wb") as out:
    writer(out, schema, records)
