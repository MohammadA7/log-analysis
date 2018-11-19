import DBLog


def printMostPopularThreeArticlesAllTime():
    print("What are the most popular three articles of all time?")
    for article in DBLog.getMostPopularThreeArticlesAllTime():
        print("\"{}\" -- {} views".format(article[0], article[1]))


def printMostPopularAuthorsAllTime():
    print("Who are the most popular article authors of all time? ")
    for author in DBLog.getMostPopularAuthorsAllTime():
        print("{} -- {} views".format(author[0], author[1]))


def printWhichDaysHaveErrorsMoreThan1Percent():
    print("On which days did more than 1% of requests lead to errors? ")
    for day in DBLog.getWhichDaysHaveErrorsMoreThan1Percent():
        print("\"{}\" -- {}% errors".format(day[0], day[1]))


printMostPopularThreeArticlesAllTime()
printMostPopularAuthorsAllTime()
printWhichDaysHaveErrorsMoreThan1Percent()
