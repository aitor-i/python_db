import sqlite3

my_connection = sqlite3.connect("Product_management")

my_cursor = my_connection.cursor()

# my_cursor.execute('''
#     CREATE TABLE PRODUCTS (
#         ARTICLE_ID VARCHAR(4) PRIMARY KEY,
#         ARTICLE_NAME VARCHAR(50),
#         ARTICLE_PRICE INTEGER,
#         ARTICLE_SECTON VARCHAR(20)
#     )

# ''')

# products = [

#     ("0001", "Ball", 10, "Toy"),
#     ("0002", "Trousers", 25, "Cloth"),
#     ("0003", "Wrench", 60, "Tool"),
#     ("0004", "Lorry", 15, "Toy")
# ]

# my_cursor.executemany("INSERT INTO PRODUCTS VALUES (?,?,?,?)", products)


# my_cursor.execute("SELECT * FROM PRODUCTS")
# products_output = my_cursor.fetchall()

# print(products_output)

my_connection.commit()
my_connection.close()
