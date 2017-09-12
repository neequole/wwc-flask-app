import sqlite3 as lite
import sys

quotes = [
    "'If people do not believe that mathematics is simple, it is only because they do not realize how complicated life is.' -- John Louis von Neumann ",
    "'Computer science is no more about computers than astronomy is about telescopes' --  Edsger Dijkstra ",
    "'To understand recursion you must first understand recursion..' -- Unknown",
    "'You look at things that are and ask, why? I dream of things that never were and ask, why not?' -- Unknown",
    "'Mathematics is the key and door to the sciences.' -- Galileo Galilei",
    "'Not everyone will understand your journey. Thats fine. Its not their journey to make sense of. Its yours.' -- Unknown"
]
con = lite.connect('helloworld.db')

with con:
    cur = con.cursor()
    try:
        cur.execute("CREATE TABLE Quotes(Id INT, quote TEXT)")
    except lite.OperationalError as e:
        pass
    for i in range(len(quotes)):
        query = "INSERT INTO Quotes VALUES({}, \"{}\")".format(i+1, quotes[i])
        cur.execute(query)
