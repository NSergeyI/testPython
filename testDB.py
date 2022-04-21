import sqlite3
from pprint import pprint as pp

conn = sqlite3.connect("datafile.db")
cursor = conn.cursor()
# cursor.execute("create table people (id integer primary key, name text,count integer)")
# cursor.execute("insert into people (name, count) values ('Bob', 1)")
# cursor.execute("insert into people (name, count) values (?, ?)", ("Jill", 15))
# cursor.execute("insert into people (name, count) values (:username, :usercount)", {"username": "Joe", "usercount": 10})
# conn.commit()

# result = cursor.execute("select * from people")
# print(result.fetchall())
# result = cursor.execute("select * from people where name like :name", {"name": "bob"})
# cursor.execute("update people set count=? where name=?", (20, "Jill"))
# conn.commit()
result = cursor.execute("select * from people")
for row in result:
    print(row)
# pp(result.fetchall())
# print(cursor)
# pp(cursor)
