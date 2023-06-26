def search_records(pattern):
#     conn = psycopg2.connect(database="postgres", user="postgres", password="qwerty123", host="localhost")
#     cursor = conn.cursor()
#     cursor.execute(f"SELECT * FROM phonebook_1 WHERE name LIKE '%{pattern}%' OR number LIKE '%{pattern}%'")
#     records = cursor.fetchall()
#     conn.close()
#     return records

# records = search_records('80000')
# print(records)