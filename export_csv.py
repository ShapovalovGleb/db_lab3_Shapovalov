import csv
import psycopg2

username = 'postgres'
password = '110603'
database = 'Shapovalov_Lab3'
host = 'localhost'
port = '5432'

OUTPUT_FILES = 'Shapovalov_DB{}.csv'
TABLES = ['Shows', 'Genres', 'Production', 'ShowScoreDate',]

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()

    for table_name in TABLES:
        cur.execute('SELECT * FROM ' + table_name)
        fields = [x[0] for x in cur.description]
        with open(OUTPUT_FILES.format(table_name), 'w') as outfile:
            writer = csv.writer(outfile)
            writer.writerow(fields)
            for row in cur:
                writer.writerow([str(x) for x in row])