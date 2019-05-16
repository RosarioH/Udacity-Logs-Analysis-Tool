#!/usr/bin/env python3
import psycopg2


def fetch_all(query):
    db = psycopg2.connect("dbname=news")
    conn = db.cursor()
    conn.execute(query)
    all_results = conn.fetchall()
    db.close()
    return all_results


def top_three_articles():
    article_query = """
    SELECT articles.title, count(*)
    FROM log, arctiles
    WHERE log.path = concat('/article/',articles.slug)
    GROUP BY articles.title ORDER BY count(*) DESC limit 3;
    """
    result = fetch_all(article_query)
    output = '  %s: %s Views\n'
    top_three_articles = "".join(
        output % (Article.capitalize(), views)
        for Article, views in result)
    print("\n1.Three of the most popular articles of all time:\n ")
    print(top_three_articles)


def top_authors():
    article_query = """
    Select authors.name AS authors, count(*) AS views FROM log,
    articles, authors WHERE log.path = concat('/article/', articles.slug)
    AND articles.author = authors.id
    GROUP BY authors.name ORDER BY count(*) DESC;
    """
    result = fetch_all(article_query)
    output = '  %s: %s Veiws\n'
    top_authors = "".join(
        output % (Authors, Views) for Authors, Views in result)
    print("\n2.Most popular article authors of all time:\n ")
    print(top_authors)


def percentage_error():
    error_query = '''
    WITH status_errors AS (select date(time) AS date,count(status)
    AS errors FROM log WHERE status LIKE '%404%' GROUP BY date), status_ok
    AS (SELECT date(time) AS date, count(status) AS status_200 FROM
    log WHERE status LIKE '%200%' GROUP BY date), percentage_error AS
    (SELECT status_errors.date, cast(float8(sum(status_errors.errors)/
    (sum(status_errors.errors) + sum(status_ok.status_200)))*100 AS numeric)
    AS all_errors FROM status_errors FULL JOIN status_ok on status_errors.date
    = status_ok.date GROUP BY status_errors.date ORDER BY all_errors DESC)
    SELECT * FROM percentage_error WHERE all_errors >=1;'''
    result = fetch_all(error_query)
    view = '  %s - %s errors\n'
    error = "".join(
        view % (date.strftime('%b/%d/%Y'), format(err, '.2f'))
        for date, err in result)
    print("\n3.More than one percent of requests lead to errors was on:\n ")
    print(error)


def main():
    try:
        top_three_articles()
        top_authors()
        percentage_error()
    except psycopg2.DatabaseError:
        print("Failed to connect to PostgreSQL Database.")
    except Exception:
        print("Sorry an Unknown error has occurred.")


main()
