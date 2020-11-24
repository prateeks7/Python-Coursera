import sqlite3
import re
con = sqlite3.connect('sql2.sqlite')
cur = con.cursor()

cur.execute('''CREATE TABLE Counts (
    org TEXT,
    count INTEGER
)''')

file= open('mbox.txt')

for i in file:
    if i.startswith("From: "):
        words = i.split()
        email = re.findall('@(.*)',words[1])
        cur.execute('SELECT count FROM Counts WHERE org=?',(email[0],))
        c=cur.fetchone()
        if c is None:
            cur.execute('INSERT INTO Counts (org,count) VALUES (?,1)',(email[0],))
        else:
            cur.execute('UPDATE Counts SET count = count+1 WHERE org=?',(email[0],))
    con.commit()
cur.close()
