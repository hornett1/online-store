import sqlite3

con = sqlite3.connect("store.db")

cursor = con.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS products (
              product_id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT NOT NULL,
              category TEXT NOT NULL,
              price REAL NOT NULL
              )""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS customers ( 
               customer_id INTEGER PRIMARY KEY AUTOINCREMENT, 
               first_name TEXT NOT NULL, 
               last_name TEXT NOT NULL, 
               email TEXT NOT NULL UNIQUE 
               )""")

cursor.execute(""" CREATE TABLE IF NOT EXISTS orders ( 
               order_id INTEGER PRIMARY KEY AUTOINCREMENT,
               customer_id INTEGER NOT NULL, 
               product_id INTEGER NOT NULL, 
               quantity INTEGER NOT NULL, 
               order_date DATE NOT NULL, 
               FOREIGN KEY (customer_id) REFERENCES customers(customer_id), 
               FOREIGN KEY (product_id) REFERENCES products(product_id)
               )""")




















while True:
    print("\nSelect option below")
    print("1 - Add customers, products, orders to database(REQUIRED)")
    print("2 - Summary sales review")
    print("3 - Number of orders per customer")
    print("4 - Average order check")
    print("5 - The most popular category of goods")
    print("6 - The total number of products in each category")
    print("7 - Update the prices of products in the 'Phones' category by 10%")
    print("8 - Save changes in database")
    print("9 - Quit")

    choice = input()

    if choice == "1":
        cursor.executemany(""" INSERT INTO products(name, category, price) VALUES(?,?,?)""", [
        ("Asus Legion", "Notebooks", 499),
        ("iPhone XXX", "Phones", 1599),
        ("iPad Pro", "Tablets", 1399),
        ("Deer", "eAnimals", 150000000)])

        cursor.executemany(""" INSERT INTO customers(first_name, last_name, email) VALUES(?,?,?)""",
        [
            ("John", "Smith", "johnsmith@gmail.com"),
            ("Santa", "Barbara", "sb@gmail.com"),
            ("Santa", "Claus", "santa10claus@gmail.com"),
            ("Kenny", "White", "ken_white@gmail.com")
        ]
        )

        cursor.executemany(""" INSERT INTO orders(customer_id, product_id, quantity, order_date) VALUES(?,?,?,?)""",
                        [
                            (1, 1, 1, "20.08.2024"),
                            (2, 1, 3, "27.06.1994"),
                            (3, 4, 7, "30.12.1999")
                        ])
        
        print("Done!")

    elif choice == "2":
        cursor.execute(""" SELECT SUM(products.price), products.name FROM products INNER JOIN orders ON orders.order_id=products.product_id  GROUP BY orders.product_id""")
        
        print(cursor.fetchall())

    elif choice == "3":
        cursor.execute(""" 
        SELECT customers.first_name, customers.last_name, COUNT(orders.order_id)
        FROM customers
        INNER JOIN orders ON customers.customer_id = orders.customer_id
        GROUP BY customers.customer_id
        """)

        print(cursor.fetchall())

    elif choice == "4":
        cursor.execute("""
        WITH OrderTotals AS (
            SELECT orders.order_id, SUM(products.price * orders.quantity) AS total_amount
            FROM orders
            INNER JOIN products ON orders.product_id = products.product_id
            GROUP BY orders.order_id
        )
        SELECT AVG(total_amount) AS average_order_amount
        FROM OrderTotals
        """)

        print(cursor.fetchall())

    elif choice == "5":
        cursor.execute("""
        WITH CategoryOrderCounts AS (
            SELECT products.category, COUNT(orders.order_id) AS order_count
            FROM orders
            INNER JOIN products ON orders.product_id = products.product_id
            GROUP BY products.category
        )
        SELECT category, order_count
        FROM CategoryOrderCounts
        ORDER BY order_count DESC
        LIMIT 1
        """)

        print(cursor.fetchall())

    elif choice == "6":
        cursor.execute("""
        SELECT category, COUNT(*) AS product_count
        FROM products
        GROUP BY category
        """)

        print(cursor.fetchall())

    elif choice == "7":
        cursor.execute("""
        UPDATE products
        SET price = price * 1.10
        WHERE category = 'Phones'
        """)

        print("Done!")

    elif choice == "8":
        con.commit()
        print("Saved!")

    elif choice == "9":
        break

    else:
        print("Incorrect input")

