import psycopg2


hostname='localhost'
database='demo'
username='postgres'    
pwd='136300'
port_id='5433'
cur=None
conn=None
try:
    conn=psycopg2.connect(
        host= hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id)
    
    cur=conn.cursor() #командалар орындайтын окстык
    
    cur.execute('DROP TABLE IF EXISTS data')



    create_table='''CREATE TABLE IF NOT EXISTS data(
    id int PRIMARY KEY,
    name varchar(40),
    phone varchar(30),
    hometown varchar(30))'''

    cur.execute(create_table)

    insert_values='INSERT INTO data(id,name,phone,hometown) VALUES(%s,%s,%s,%s)'
    n=int(input('How many employee there are:'))
    a=[]
    for i in range(n):
        id=int(input('input id:'))
        name=(input('input name:'))
        phone=int(input('input phone:'))
        hometown=(input('input homotown:'))
        a.append((id,name,phone,hometown))
    for i in a:
        cur.execute(insert_values,i)
    conn.commit()

    cur.execute('SELECT * FROM data')
    for row in cur.fetchall():# fetchall() крч селект дегенде не шыгатынын корсетеди
        print(row)
    column=input('What employee\'s data u want to update:')
    to_change=input("what column change:")
    for_what=input("for what:")
    cur.execute(f'UPDATE data SET {to_change}=\'{for_what}\' WHERE  name=\'{column}\'')

    phone_to_delete=input()
    cur.execute(f'DELETE FROM data WHERE phone=\'{phone_to_delete}\'')



    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
