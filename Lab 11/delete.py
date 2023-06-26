import psycopg2



# print('Enter your name')
# name=input()
# print('Enter your phone number')
# number=input()

# try:
#     connection=psycopg2.connect(user='postgres',password='qwerty123',host='localhost',port='5432',database='postgres')
#     cursor=connection.cursor()
#     cursor.execute('INSERT INTO phonebook_1 VALUES(%s,%s)',(name,number))
#     connection.commit()
#     print(cursor.fetchall())
# except (Exception) as error:
#     print(error)
# finally:
#     if connection:
#         cursor.close()
#         connection.close()


# connection = psycopg2.connect(
#     host="localhost",
#     database="postgres",
#     user="postgres",
#     password="qwerty123"
# )
# cursor = connection.cursor()
# def delete_data(name, number):
#     cursor.execute(f'DELETE FROM phonebook_1 WHERE {name} = %s', (number,))
#     connection.commit()

# # delete_data("name", "Naruto")

# delete_data("number", "87000000000")

# cursor.close()
# connection.close()




def query_with_pagination(limit, offset):
    conn = psycopg2.connect(
        host="localhost",
        database="postgres",
        user="postgres",
        password="qwerty123"
    )
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM phonebook_1 LIMIT {limit} OFFSET {offset}")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

result = query_with_pagination(5, 0)
print(result)


 
# conn = psycopg2.connect(
#     database="postgres",
#     user='postgres',
#     password='qwerty123',
#     host='localhost'
# )
# conn.autocommit = True
 
# cursor = conn.cursor()

# cursor.execute('''insert into phonebook_1(name , number)
# values('Miku', 123),('Nino',81); ''')
 
# conn.commit()
# conn.close()





# def search_records(pattern):
#     conn = psycopg2.connect(database="postgres", user="postgres", password="qwerty123", host="localhost")
#     cursor = conn.cursor()
#     cursor.execute(f"SELECT * FROM phonebook_1 WHERE name LIKE '%{pattern}%' OR number LIKE '%{pattern}%'")
#     records = cursor.fetchall()
#     conn.close()
#     return records

# records = search_records('80000')
# print(records)