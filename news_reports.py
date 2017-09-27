# Python 2.7.12 or Higher
import psycopg2

DBNAME = "news"

POPULAR_ARTICLES_QUERY = """
select a.title, count(l.id) as views
from articles a left join log l
on concat('/article/',a.slug) = l.path
group by a.title 
order by views desc
limit 3;
"""
AUTHOR_RANKING_QUERY = """
select au.name, count(l.id) as views
from authors au
left join articles ar on ar.author = au.id
left join log l on concat('/article/',ar.slug) = l.path
group by au.id
order by views desc;
"""
ERRONEOUS_DAY_QUERY = """
select to_char(error_summary.date, 'Mon DD, YYYY') date, 
round((error_size::float * 100/all_size)::numeric, 2) percent 

from (select time::date as date, count(id) error_size
    from log 
    where status != '200 OK'
    group by date) as error_summary

left join (select time::date date, count(id) all_size 
from log 
group by date) as all_summary

on error_summary.date = all_summary.date

where error_size::float * 100/all_size > 1
order by percent desc;
"""

def show_popular_articles():
    """Print out the top 3 articles by popularity among website visitors"""
    cursor = DB_CONNECTION.cursor()
    cursor.execute(POPULAR_ARTICLES_QUERY)
    results = cursor.fetchall()

    print("POPULAR ARTICLES")
    print("-------------------------------")
    for title, views in results:
        print("%s - %s views" % (title, views))
    print("\r\n")


def show_authors_by_popularity():
    """List out all authors based on popularity
    (how many visits their articles have cummulatively)"""
    cursor = DB_CONNECTION.cursor()
    cursor.execute(AUTHOR_RANKING_QUERY)
    results = cursor.fetchall()

    print("POPULAR AUTHORS")
    print("-------------------------------")
    for name, views in results:
        print("%s - %s views" % (name, views))
    print("\r\n")


def show_high_error_days():
    """Print out any days where HTTP error responses
    exceed 1% of all requests, along with the percentage"""
    cursor = DB_CONNECTION.cursor()
    cursor.execute(ERRONEOUS_DAY_QUERY)
    results = cursor.fetchall()


    print("HIGH ERROR DAYS")
    print("-------------------------------")
    for date, percent in results:
        print("%s - %s%% errors" % (date, percent))
    print("\r\n")


if __name__ == '__main__':
    """Print out all the statistics"""
    DB_CONNECTION = psycopg2.connect(database=DBNAME)
    show_popular_articles()
    show_authors_by_popularity()
    show_high_error_days()
    DB_CONNECTION.close()
