import matplotlib.pyplot as plt
import psycopg2

username = 'postgres'
password = '110603'
database = 'Shapovalov_Lab3'
host = 'localhost'
port = '5432'

query_1 = '''
SELECT production_name, COUNT(shows.show_id) 
FROM (Production JOIN shows ON shows.production_id = Production.production_id) GROUP BY production_name
'''

query_2 = '''
SELECT genre_name, COUNT(shows.show_id) 
FROM (Genres JOIN shows ON shows.genre_id = genres.genre_id) GROUP BY genre_name
'''

query_3 = '''
SELECT release_year, COUNT(shows.show_id) FROM shows GROUP BY release_year ORDER BY release_year
'''

conn = psycopg2.connect(user=username, password=password, dbname=database, host=host, port=port)

with conn:
    cur = conn.cursor()
    cur.execute(query_1)
    country = []
    shows_count = []
    for row in cur:
        shows_count.append(row[0])
        country.append(row[1])
    figure, (bar_ax, pie_ax, graph_ax) = plt.subplots(1, 3)
    x_range = range(len(country))
    bar_ax.bar(x_range, country, label='Count')
    bar_ax.set_title('Shows count')
    bar_ax.set_xlabel('Country')
    bar_ax.set_ylabel('Count')
    bar_ax.set_xticks(x_range)
    bar_ax.set_xticklabels(shows_count,  rotation=90)

    cur.execute(query_2)
    genres = []
    total_count = []
    for row in cur:
        genres.append(row[0])
        total_count.append(row[1])
    pie_ax.pie(total_count, labels=genres, autopct='%1.1f%%')
    pie_ax.set_title('The part of each genre')

    cur.execute(query_3)
    count = []
    release_years = []
    for row in cur:
        count.append(row[0])
        release_years.append(row[1])

    graph_ax.plot(count, release_years, marker='*')
    graph_ax.set_xlabel('Release year')
    graph_ax.set_ylabel('Count')
    graph_ax.set_title('Shows count by release year')

    for cnt, r_y in zip(count, release_years):
        graph_ax.annotate(r_y, xy=(cnt, r_y), xytext=(7, 2), textcoords='offset points')


mng = plt.get_current_fig_manager()
mng.resize(1400, 600)
plt.show()