# !/usr/bin/env python3
import psycopg2

def fetch_all(query):
    db = psycopg2.connect("dbname=news")
    conn = db.cursor()
    conn.execute(query)
    all_results = conn.fetchall()
    db.close()
    return all_results



def top_three_articles():
    article_query = "select substr(path,10) as Article, count(*) as views from log where path !='/' group by path order by views desc limit 3;"
    result = fetch_all(article_query)
    output = '  %s: %s Views\n'
    top_three_articles = "".join(output % (Article.capitalize(), views) for Article, views in result)
    print("\n1.Three of the most popular articles of all time:\n ")
    print (top_three_articles)

def top_authors():
    article_query = """select authors.name as Authors, count(*) as Views from log, articles, authors where log.path ='/article/' || articles.slug and articles.author = authors.id
                       group by authors.name order by count(*) desc;
                    """
    result = fetch_all(article_query)
    output = '  %s: %s Veiws\n'
    top_authors = "".join(output % (Authors,Views) for Authors, Views in result)
    print("\n2.Most popular article authors of all time:\n ")
    print (top_authors)

def percentage_error():
    error_query = ''' WITH status_errors as (select date(time) as date, count(status) as errors from
    log where status like '%404%' group by date),
    status_ok as (select date(time) as date, count(status) as status_200 
    from log where status like '%200%' group by date),
    percentage_error as (select status_errors.date, 
    cast(float8 (sum(status_errors.errors)/(sum(status_errors.errors) + sum(status_ok.status_200)))*100 as numeric) as all_errors
    from status_errors full join status_ok on status_errors.date = status_ok.date group by status_errors.date order by all_errors desc)
    select * from percentage_error where all_errors >=1;'''
    result = fetch_all(error_query)
    view = '  %s - %s errors\n'
    error = "".join(view % (date.strftime('%b/%d/%Y'), format(err, '.2f')) for date, err in result)
    print("\n3.More than one percent of requests lead to errors was on:\n ")
    print(error)

def main():
    top_three_articles()
    top_authors()
    percentage_error()

main()
