
import sqlite3 as sql


s=input ('���� �������� ���� ������: ')                                            #input name for a new db
con=sql.connect(s+'.db')
sch=int(input('������� ���������� ���������� � ������� (� ������): '))         #quantity column given by admin
p=0

with con:
    cur=con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS 'test' (id INTEGER)")
    for sch in p:
        nam_tab=input('��� �������: ')
        cur.execute("ALTER TABLE IF NOT EXISTS 'test' (", nam_tab, " INTEGER)")
        con.commit()
