import psycopg2

conn = psycopg2.connect( "dbname='pycamp_201705' user='pycamp' host ='localhost' password='pycamp'" )

cur = conn.cursor()

cur.execute('create table news ( news_id serial primary key, date varchar, title varchar, category varchar, link varchar );' )

conn.commit()

