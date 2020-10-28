import pymysql

conn = pymysql.connect('localhost', 'root', 'vikalp')
cur = conn.cursor()
v='1 or 0=0'
cur.execute(f"SELECT IF(0={v}, 'YES', 'NO')")
print(cur.fetchone())
