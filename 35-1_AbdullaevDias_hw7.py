import sqlite3 as hw_db

with hw_db.connect('hw.db') as con:
    cur = con.cursor()
    cur.execute(""" CREATE TABLE IF NOT EXISTS products(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    product_title TEXT VARCHAR(200) NOT NULL,
    price FLOAT(10, 2) NOT NULL DEFAULT 0.00,
    quantity INTEGER NOT NULL DEFAULT 0)
""")


def create_product(con, product: tuple):
    sql = """INSERT INTO products
    (product_title, price, quantity)
    VALUES (?, ?, ?)"""
    cursor = con.cursor()
    cursor.execute(sql, product)
    con.commit()


create_product(con, ('Bed', 200.20, 100))
create_product(con, ('Bath', 400.69, 20))
create_product(con, ('TV', 3000.90, 2))
create_product(con, ('TV_SUPER', 1000.60, 1))
create_product(con, ('Teapot', 1000.80, 40))
create_product(con, ('Cooker', 100.20, 5))
create_product(con, ('Cupboard', 300.22, 5))
create_product(con, ('Freezer_SUPER', 1000.97, 20))
create_product(con, ('Fridge', 1920.99, 9))
create_product(con, ('Microwave', 2000.40, 40))
create_product(con, ('Pan', 70.60, 60))
create_product(con, ('Washing machine', 1000.29, 35))
create_product(con, ('Мыльное мыло', 40.31, 3))
create_product(con, ('мыло жидкое', 50, 50))
create_product(con, ('мыло', 60, 1))
create_product(con, ('мыло', 50, 10))
create_product(con, ('Супер мыло', 50, 10))


def change_quatity(con, new_quantity, product_id):
    sql = """UPDATE products SET quantity = ? WHERE id = ? """
    cursor = con.cursor()
    cursor.execute(sql, (new_quantity, product_id))
    con.commit()


def change_price(con, new_price, product_id):
    sql = """UPDATE products SET price = ? WHERE id = ?"""
    cursor = con.cursor()
    cursor.execute(sql, (new_price, product_id))
    con.commit()


def delete_products(con, product_id):
    sql = """DELETE FROM products WHERE id = ?"""
    cursor = con.cursor()
    cursor.execute(sql, (product_id,))
    con.commit()


def select_all_products(con):
    sql = """SELECT * FROM products"""
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(row)


def serch_product():
    sql = """SELECT * FROM products WHERE price < 100 and quantity > 5"""
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(f'Товары которые дешевли 100 сомов: {row}')


def serch_name_product():
    sql = """SELECT * FROM products WHERE product_title LIKE '%мыло%'"""
    cursor = con.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    for row in rows:
        print(f'Товары который вы ищете:  {row}')


change_price(con, 40.31, 15)
change_quatity(con, 1, 2)
delete_products(con, 590)
serch_product()
serch_name_product()
select_all_products(con)


con.close()