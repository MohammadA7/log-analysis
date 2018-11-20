#!/usr/bin/python3

import DBLog


def printMostPopularThreeArticlesAllTime():
    print("What are the most popular three articles of all time?\n")
    for article in DBLog.getMostPopularThreeArticlesAllTime():
        print("\"{}\" -- {} views".format(article[0], article[1]))


def printMostPopularAuthorsAllTime():
    print("\nWho are the most popular article authors of all time?\n")
    for author in DBLog.getMostPopularAuthorsAllTime():
        print("{} -- {} views".format(author[0], author[1]))


def printWhichDaysHaveErrorsMoreThan1Percent():
    print("\nOn which days did more than 1% of requests lead to errors?\n")
    for day in DBLog.getWhichDaysHaveErrorsMoreThan1Percent():
        print("\"{}\" -- {}% errors".format(day[0], day[1]))


printMostPopularThreeArticlesAllTime()
printMostPopularAuthorsAllTime()
printWhichDaysHaveErrorsMoreThan1Percent()
