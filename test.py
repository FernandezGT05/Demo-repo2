import sqlite3

with sqlite3.connect('database.db') as conn:
    cur=conn.cursor()
    # cur.execute("INSERT INTO sellers(seller_id,seller_name,age) VALUES('sell04','hanma',47)")
    # cur.execute("INSERT INTO sellers(seller_id,seller_name,age) VALUES('sell05','baki',21)")
    # cur.execute("SELECT * FROM customers")
    # rows=cur.fetchall()
    # for row in rows:
    #     print(row)
    # # cur.execute("UPDATE sellers SET seller_name=? WHERE seller_name=?",('patrick','trick'))
    # # cur.execute("DELETE FROM customers WHERE first_name=?",('John',))
    # # cur.execute("UPDATE sellers SET seller_id=? WHERE age=?",('sell01',20))
    # cur.execute("SELECT *FROM sellers WHERE seller_id=?",('sell01',))
    # line=cur.fetchone()
    # print(line)
    # cur.execute("""CREATE TABLE IF NOT EXISTS example(
    #             field1 PRIMARY KEY,
    #             field2 TEXT NOT NULL,
    #             field3 INTEGER UNIQUE NOT NULL)""")
    # cur.execute("INSERT INTO example(field1,field2,field3) VALUES(22212,'2222',22122)")
    cur.execute("SELECT field3 FROM example WHERE field2=?",('2222',))
    # cur.execute("DELETE FROM example WHERE field1=?",(2222,))
    # cur.execute("DROP TABLE IF EXISTS example")
    rows=cur.fetchall()
    for row in rows:
        for x in row:
            print(x)

    