import psycopg2

def create_table_and_insert_data():
    conn = psycopg2.connect(
        host='localhost',
        dbname='demo',
        user='postgres',
        password='136300',
        port='5433'
    )
    cur = conn.cursor()

    
    cur.execute('''
        CREATE TABLE IF NOT EXISTS PhoneBook (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            surname VARCHAR(50),
            phone_number VARCHAR(20)
        )
    ''')

    
    sample_data = [
        ('Emel', 'Azim', '1234567890'),
        ('Darkhan', 'Azhibek', '9876543210')
    ]

    for person in sample_data:
        cur.execute('''
            INSERT INTO PhoneBook(name, surname, phone_number)
            VALUES (%s, %s, %s)
        ''', person)

    conn.commit()
    cur.close()
    conn.close()

def search_phonebook(pattern):
    conn = psycopg2.connect(
        host='localhost',
        dbname='demo',
        user='postgres',
        password='136300',
        port='5433'
    )
    cur = conn.cursor()

    query = """
    SELECT id, name, surname, phone_number
    FROM PhoneBook
    WHERE name ILIKE %s
       OR surname ILIKE %s
       OR phone_number ILIKE %s
    """
    wildcard_pattern = f"%{pattern}%"
    cur.execute(query, (wildcard_pattern, wildcard_pattern, wildcard_pattern))
    results = cur.fetchall()

    cur.close()
    conn.close()

    return results



create_table_and_insert_data()
pattern_input = input("Enter search pattern: ")
results = search_phonebook(pattern_input)

print("\nMatching Records:")
for r in results:
    print(r)
