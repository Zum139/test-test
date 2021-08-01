import hashlib as hash
import os
import sqlite3 as sql


p=0
users = {} # Simple user cargo
# Add a user
username = 'Loki'
password = 'mypassword'

def new_db():
    s=input ('name for a new db: ') #input name for a new db
    con=sql.connect(s+'.db')


def tab_wr():                 #add a new record to table
    sch=int(input('set the number of columns(integer): ')) #ask quantity column
    tab=sql.connect('users.db')
    with tab:
        cur=tab.cursor()
        for sch in p:
            nam_tab=input('��� �������: ')
            cur.execute("ALTER TABLE IF NOT EXISTS 'test' (", nam_tab, " INTEGER)")
            con.commit()


def creat_pass_user():
    salt = os.urandom(32) # new salt for user
    key = hash.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 100000)
    users[username] = {'salt': salt, 'key': key}

    a = input('password please: ')
    aa = hash.pbkdf2_hmac('sha256', a.encode('utf-8'), salt, 100000)
    '''
    aaa[username] = {'salt': salt, 'key': aa} # is not important the string actually
    '''

    if aa == key:
        print('well done')


'''
#ниже блок кода для работы с базой
#создаем подключение к БД
db = MySQLdb.connect(host="localhost", user="vash_user", passwd="vash_pass", db="py", charset='utf8')
#используя метод cursor() получаем объект для работы с базой
cursor = db.cursor()
#формируем sql запрос на запись
sql = """INSERT INTO zp(zp)
        VALUES ('%(zarplata)s')
        """%{"zarplata":av_zp}
# исполняем SQL-запрос
cursor.execute(sql)
# применяем изменения к базе данных
db.commit()
''' #add a value to table to the db


'''
 начал создавать возможность сохранять имя и пароль с солью в БД, но заебался,
 понакидал всякой хуйни с ранних наработок, завтра разбиру это дерьмо
'''

abc = input('what now? ')   #add the value for

if abc == 'tab_wr': tab_wr()
elif abc == 'creat_pass_user': creat_pass_user()
elif abc == 'cr_p_u': creat_pass_user()
elif abc == 'new_db': new_db()
