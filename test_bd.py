import MySQLdb

conn = MySQLdb.connect("dezeltor.mysql.tools",
                       "dezeltor_test1",
                       "Lala280508",
                       "dezeltor_test1")

cursor = conn.cursor()


# cursor.execute("""INSERT INTO test1 ( timstam, number_dk, value) VALUES ('1000', '1000', '1000')""")

# conn.commit()
cursor.execute("SELECT  `number_dk`, `value` FROM `test1` WHERE 1")
row = cursor.fetchall()
print(row)


conn.close()
