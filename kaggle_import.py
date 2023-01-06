import csv
import psycopg2

username = 'postgres'
password = '110603'
database = 'Shapovalov_Lab3'
host = 'localhost'
port = '5432'

INPUT_CSV_FILE = 'best_movies_netflix.csv'

deleting = '''
DELETE FROM Shows;
DELETE FROM Genres;
DELETE FROM Production;
DELETE FROM ShowScoreDate;
'''

insert_genres = '''
INSERT INTO Genres(genre_id, genre_name) VALUES(%s, %s)
'''

insert_production = '''
INSERT INTO Production(production_id, production_name) VALUES(%s, %s)
'''

insert_shows = '''
INSERT INTO Shows(show_id, title, release_year, genre_id, duration, production_id) VALUES(%s, %s, %s, %s, %s, %s)
'''

insert_showscoredate = '''
INSERT INTO ShowScoreDate(show_id, last_update, number_of_votes, score) VALUES(%s, %s, %s, %s)
'''

conn = psycopg2.connect(user=username, password=password, dbname=database)

with conn:
    cur = conn.cursor()
    cur.execute(deleting)
    with open(INPUT_CSV_FILE, 'r') as inf:
        reader = csv.DictReader(inf)
        genres_list = []
        productions_list = []
        for idx, row in enumerate(reader):
            if row['main_genre'] not in genres_list:
                genres_list.append(row['main_genre'])
                cur.execute(insert_genres, (genres_list.index(row['main_genre'])+1, row['main_genre']))
            if row['main_production'] not in productions_list:
                productions_list.append(row['main_production'])
                cur.execute(insert_production, (productions_list.index(row['main_production'])+1, row['main_production']))

            cur.execute(insert_shows, (idx+1, row['title'], row['release_year'], genres_list.index(row['main_genre'])+1, row['duration'], productions_list.index(row['main_production'])+1))
            cur.execute(insert_showscoredate, (idx+1, "30.12.2022", row['number_of_votes'], row['score']))

    conn.commit()