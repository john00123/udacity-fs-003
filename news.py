# !/usr/bin/env python
import psycopg2
dbname = "news"

# Queries


# 1. What are the most popular three articles of all time?
query1 = """
    SELECT title, count(*) as num FROM articles, log
    WHERE articles.slug = substring(log.path, 10)
    GROUP BY title ORDER BY num DESC LIMIT 3;
    """


# 2. Who are the most popular article authors of all time?
query2 = """
    SELECT authors.name, count(*) AS num
    FROM articles
    JOIN authors on articles.author = authors.id
    JOIN log on articles.slug = substring(log.path, 10)
    WHERE log.status LIKE '200 OK'
    GROUP BY authors.name ORDER BY num desc;
    """


# 3. On which days did more than 1% of requests lead to errors?
query3 = """
    SELECT *
    FROM (
        select a.day, round(cast((100 * b.issues) as numeric) /
        cast(a.issues as numeric), 2)
    AS error_per FROM (
        select date(time) as day, count(*) as issues from log group by day)
    AS a INNER JOIN (
        select date(time) as day, count(*) as issues from log
        where status like '%404%' group by day) as b on a.day = b.day)
    AS t WHERE error_per > 1.0;
    """


# Store and print results
query1_results = dict()
query1_results['title'] = (
    "1. The most popular three articles of all time?")
query1_results['ending'] = " views"

query2_results = dict()
query2_results['title'] = (
    "2. Who are the most popular article authors of all time?")
query2_results['ending'] = " views"

query3_results = dict()
query3_results['title'] = (
    "3. On which days did more than 1% of requests lead to errors?")
query3_results['ending'] = " percent"


# Get query results
def get_query_result(query):
    db = psycopg2.connect(database=dbname)
    cur = db.cursor()
    cur.execute(query)
    results = cur.fetchall()
    db.close()
    return results


# Print results method
def print_query_results(query_results):
    print (query_results['title'])
    for result in query_results['results']:
        print ('\t' + str(result[0]) + ': ' +
               str(result[1]) +
               query_results['ending'])


# Store results
query1_results['results'] = get_query_result(query1)
query2_results['results'] = get_query_result(query2)
query3_results['results'] = get_query_result(query3)


# Print query results
print_query_results(query1_results)
print_query_results(query2_results)
print_query_results(query3_results)
