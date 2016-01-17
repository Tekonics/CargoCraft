import MySQLdb


db = MySQLdb.connect(host="vps.untamemadman.pw",
                     user="me-corp_Game",
                     passwd="rZqEe7G6rJrhXvTt",
                     db="me-corp_Game"

    )
cur = db.cursor()
cur.execute("SELECT * FROM name_list")
for row in cur.fetchall():
    print row[0]
db.close()
