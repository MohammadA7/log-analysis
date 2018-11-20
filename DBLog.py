import psycopg2


def getMostPopularThreeArticlesAllTime():
    db = psycopg2.connect("dbname=news")
    query = "select title, count(*) as num from articles, log \
    where articles.slug = split_part(log.path,'/', 3) \
    group by title order by num desc limit 3;"
    cursor = db.cursor()
    cursor.execute(query)

    result = cursor.fetchall()
    db.close()

    return result


def getMostPopularAuthorsAllTime():
    db = psycopg2.connect("dbname=news")
    query = "select authors.name, count(authors.id) \
    as num from articles, log, authors \
    where articles.slug = split_part(log.path,'/', 3) \
    and articles.author = authors.id \
    group by authors.name order by num desc;"

    cursor = db.cursor()
    cursor.execute(query)

    result = cursor.fetchall()
    db.close()

    return result


def getWhichDaysHaveErrorsMoreThan1Percent():
    db = psycopg2.connect("dbname=news")
    query = """
    select to_char(allRequests.day, 'Mon DD, YYYY'),
        round(((badRequests.numOfBadRequests::decimal) * 100 /
        allRequests.totalRequests), 1) as result
        from (
            select date_trunc('day', time) as day, count(*) as numOfBadRequests
            from log where status = '404 NOT FOUND' group by day)
            as badRequests
        join (
            select date_trunc('day', time) as day, count(*) as totalRequests
            from log group by day) as allRequests on
            allRequests.day = badRequests.day
    where (((badRequests.numOfBadRequests::decimal) /
        allRequests.totalRequests) > 0.01)
        """

    cursor = db.cursor()
    cursor.execute(query)

    result = cursor.fetchall()
    db.close()

    return result
