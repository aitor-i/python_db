import sqlite3

my_connection = sqlite3.connect("Product_management_2")

my_cursor = my_connection.cursor()

my_cursor.execute('''
    CREATE TABLE PRODUCTS (
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        ARTICLE_NAME VARCHAR(50),
        ARTICLE_PRICE INTEGER,
        ARTICLE_SECTON VARCHAR(20))
''')


products = [

    ("Ball", 10, "Toy"),
    ("Trousers", 25, "Cloth"),
    ("Wrench", 60, "Tool"),
    ("Lorry", 15, "Toy")
]

my_cursor.executemany("INSERT INTO PRODUCTS VALUES (NULL,?,?,?)", products)

my_cursor.execute("SELECT * FROM PRODUCTS")
products_output = my_cursor.fetchall()

print(products_output)


my_connection.commit()
my_connection.close()
