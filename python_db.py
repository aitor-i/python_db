import sqlite3

my_connection = sqlite3.connect("First_db")

my_cursor = my_connection.cursor()
# my_cursor.execute(
#     "CREATE TABLE PRODUCTS(ARTICLE_NAME VARCHAR(50), PRICE INTEGER, SECTION VARCHAR(50))")
# my_cursor.execute("INSERT INTO PRODUCTS VALUES ('BALL', 15, 'SPORTS')")

# more_products = [

#     ("T-Shirt", 10, "SPORTS"),
#     ("Jar", 49, "TOOLS"),
#     ("Lorry", 25, "TOYS")
# ]

# my_cursor.executemany("INSERT INTO PRODUCTS VALUES (?,?,?)", more_products)

my_cursor.execute("SELECT * FROM PRODUCTS")
products_output = my_cursor.fetchall()
# print(products_output)

for product in products_output:
    print("Article name: {} Article price: {}$ Article section: {}".format(
        product[0], product[1], product[2]))


my_connection.commit()


my_connection.close()
