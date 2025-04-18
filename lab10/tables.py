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

    cur.execute('DROP TABLE IF EXISTS employee') # sql командаларды ишине жазганда орындайды



    create_table=''' CREATE TABLE IF NOT EXISTS employee(
                    id int PRIMARY KEY,
                    name varchar(40),
                    salary int)'''
    cur.execute(create_table)


    

    insert_value='INSERT INTO employee (id, name, salary) VALUES(%s,%s,%s)'#мфн берип тыгу
    values =[(1,'Yemelzhan',50000),(2,'Darkhan',50000),(3,'Noname',0)]
    for value in values:
        cur.execute(insert_value,value)
    a=input()
    cur.execute(f'SELECT {a} FROM employee')

    for column in cur.fetchall():# fetchall() крч селект дегенде не шыгатынын корсетеди
        print(column)






    conn.commit()
except Exception as error:
    print(error)
finally:
    if cur is not None:
        cur.close()
    if conn is not None:
        conn.close()
