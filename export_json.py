import json
import psycopg2

username = 'postgres'
password = '110603'
database = 'Shapovalov_Lab3'
host = 'localhost'
port = '5432'

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)
OUTPUT_FILE = 'Shapovalov_DB.json'
data = {}
with conn:
    cur = conn.cursor()

    for table in ('Shows', 'Genres', 'Production', 'ShowScoreDate'):
        cur.execute('SELECT * FROM ' + table)
        rows = []
        fields = [x[0] for x in cur.description]

        for row in cur:
            rows.append(dict(zip(fields, row)))
        data[table] = rows

with open(OUTPUT_FILE, 'w') as outf:
    json.dump(data, outf, default=str, indent=4)