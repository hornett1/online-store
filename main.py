import sqlite3

con = sqlite3.connect("store.db")

cursor = con.cursor()

# cursor.execute(""" CREATE TABLE IF NOT EXISTS products (
#               product_id INTEGER PRIMARY KEY AUTOINCREMENT,
#               name TEXT NOT NULL,
#               category TEXT NOT NULL,
#               price REAL NOT NULL
#               )""")

# cursor.execute(""" CREATE TABLE IF NOT EXISTS customers ( 
#                customer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
#                first_name TEXT NOT NULL, 
#                last_name TEXT NOT NULL, 
#                email TEXT NOT NULL UNIQUE 
#                )""")

# cursor.execute(""" CREATE TABLE IF NOT EXISTS orders ( 
#                order_id INTEGER PRIMARY KEY AUTOINCREMENT,
#                customer_id INTEGER NOT NULL, 
#                product_id INTEGER NOT NULL, 
#                quantity INTEGER NOT NULL, 
#                order_date DATE NOT NULL, 
#                FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
#                FOREIGN KEY (product_id) REFERENCES products(product_id)
#                )""")


# cursor.executemany(""" INSERT INTO products(name, category, price) VALUES(?,?,?)""", [
#     ("Asus Legion", "Notebooks", 499),
#     ("iPhone XXX", "Phones", 1599),
#     ("iPad Pro", "Tablets", 1399),
#     ("Deer", "eAnimals", 150000000)
# ])

# cursor.executemany(""" INSERT INTO customers(first_name, last_name, email) VALUES(?,?,?)""",
#  [
#      ("John", "Smith", "johnsmith@gmail.com"),
#      ("Santa", "Barbara", "sb@gmail.com"),
#      ("Santa", "Claus", "santa10claus@gmail.com"),
#      ("Kenny", "White", "ken_white@gmail.com")
#  ]
# )

# cursor.executemany(""" INSERT INTO orders(customer_id, product_id, quantity, order_date) VALUES(?,?,?,?)""",
#                    [
#                        (1, 1, 1, "20.08.2024"),
#                        (2, 1, 3, "27.06.1994"),
#                        (3, 4, 7, "30.12.1999")
#                    ])



cursor.execute(""" SELECT SUM(products.price), products.name FROM products INNER JOIN orders ON orders.order_id=products.product_id  GROUP BY orders.product_id""")
print(cursor.fetchall())

con.commit()