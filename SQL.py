import MySQLdb


db = MySQLdb.connect(host="me-corp.ga",
                     user="me-corp_Game",
                     passwd="ter3Ydd2aqeNTY24",
                     db="me-corp_Game"

    )
cur = db.cursor()
cur.execute("SELECT * name_list")
for row in cur.fetchall():
    print row[0]
db.close()
