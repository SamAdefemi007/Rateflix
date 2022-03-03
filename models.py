import sqlite3
import csv

#defining a function to create a connection to the database
def connect_db(): 
    global connection
    global cursor
    connection =sqlite3.connect("database.db")
    cursor = connection.cursor()


def create_tables():
    connect_db() 
    #The tables are dropped before recreating or updating them to avoid duplication
    connection.execute("DROP TABLE IF EXISTS movie")
    connection.execute("CREATE TABLE movie (MOVIE_ID INTEGER PRIMARY KEY AUTOINCREMENT,MOVIE_TITLE TEXT, DIRECTOR TEXT, CAST TEXT, COUNTRY INTEGER, RELEASE_YEAR DATETIME, DESCRIPTION TEXT, GENRE TEXT, TYPE TEXT, TV_RATING TEXT)")
    connection.execute("DROP TABLE IF EXISTS ratings")
    connection.execute("CREATE TABLE ratings ( MOVIE_ID INTEGER, RATING FLOAT, NUMBER_OF_VOTES INTEGER, YEAR_ADDED DATETIME, FOREIGN KEY(MOVIE_ID) REFERENCES movie(MOVIE_ID))")
    connection.execute("DROP TABLE IF EXISTS users")
    connection.execute("CREATE TABLE users ( ID INTEGER PRIMARY KEY AUTOINCREMENT, FIRSTNAME TEXT, LASTNAME TEXT, EMAIL TEXT, PASSWORD TEXT,  FAVORITE_GENRE TEXT, MOVIE_ID INTEGER, FOREIGN KEY(MOVIE_ID) REFERENCES movie(MOVIE_ID))")


create_tables()
