import psycopg2

try:
    conn = psycopg2.connect(
        dbname="demo",     # or the name of your custom database
        user="postgres",       # default user
        password="136300",  # the password you set during installation
        host="localhost",
        port="5433"
    )
    print("Hello world!")
    conn.close()
except Exception as e:
    print("❌ Connection failed:")
    print(e)