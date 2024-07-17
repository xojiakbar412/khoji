##jalolov xojiakbar


import psycopg2 


#1 - misol

db_params = {
    'db_name' : 'new_db',
    'user' : 'postgres',
    'password' : 'secret',
    'host' : 'local_host',
    'port' : '5432'
}

def create_table():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    create_table_query = '''
    CREATE TABLE IF NOT EXISTS Product (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price DECIMAL NOT NULL,
        color VARCHAR(50),
        image TEXT
    )
    '''

    cursor.execute(create_table_query)
    conn.commit()

    print("Table created successfully")

    cursor.close()
    conn.close()

if __name__ == "__main__":
    create_table()


#2 - misol

def insert_product(name, price, color, image):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    insert_query = '''
    INSERT INTO Product (name, price, color, image) VALUES (%s, %s, %s, %s)
    '''

    cursor.execute(insert_query, (name, price, color, image))
    conn.commit()
    print("Product inserted successfully")

    cursor.close()
    conn.close()

def select_all_products():
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    select_query = 'SELECT * FROM Product'
    cursor.execute(select_query)
    products = cursor.fetchall()

    for product in products:
        print(product)

    cursor.close()
    conn.close()

def update_product(product_id, name, price, color, image):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    update_query = '''
    UPDATE Product
    SET name = %s, price = %s, color = %s, image = %s
    WHERE id = %s
    '''

    cursor.execute(update_query, (name, price, color, image, product_id))
    conn.commit()
    print("Product updated successfully")

    cursor.close()
    conn.close()


def delete_product(product_id):
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    delete_query = 'DELETE FROM Product WHERE id = %s'
    cursor.execute(delete_query, (product_id,))
    conn.commit()
    print("Product deleted successfully")

    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_table()
    



#3 - misol

class Alphabet:
    def __init__(self):
        self.letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.index = 0

    def __iter__(self):
        return self
    

    def __next__(self):
        if self.index < len(self.letters):
            letter = self.letters[self.index]
            self.index += 1
            return letter
        else:
            raise StopIteration
        
if __name__ == '__main__':
    alphabet = Alphabet()
    for letter in alphabet:
        print(letter)


#4 - misol

import threading
import time

def print_numbers():
    for i in range (1, 6):
        print(i)
        time.sleep(1)

def print_letters():
    for letter in "ABCDE":
        print(letter)
        time.sleep(1)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)

t1.start()
t2.start()

t1.join()
t2.join()

#5 - misol

import sqlite3

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def save(self):
        connection = sqlite3.connect('products.db')
        cursor = connection.cursor()

        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                name TEXT,
                price REAL,
                quantity INTEGER
            )
        ''')


        cursor.execute('''
            INSERT INTO products (name, price, quantity)
            VALUES (?, ?, ?)
        ''', (self.name, self.price, self.quantity))


        connection.commit()
        connection.close()

product = Product('Artel tv', 200.00, 5)

product.save()

print("Product database ga saqlandi")


#6 - misol

import psycopg2
from psycopg2 import sql

class DbConnect:
    def __init__(self, dsn):
        self.dsn = dsn
        self.conn = None
        self.cur = None

    def __enter__(self):
        self.conn = psycopg2.connect(self.dsn)
        self.cur = self.conn.cursor()
        return self.conn, self.cur
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cur is not None:
            self.cur.close()
        if self.conn is not None:
            self.conn.close()

dsn = "dbname=new_db user=postgres password=secret host=localhost port=5432"

with DbConnect(dsn) as (conn, cur):
    cur.execute("SELECT version();")
    print(cur.fetchone())




#7 - misol

import requests
import sqlite3

class Product:
    def __init__(self, id, title, description, price, brand, category):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.brand = brand
        self.category = category

    def save(self):
        connection = sqlite3.connect('products.db')
        cursor = connection.cursor()

        # Create table if it doesn't exist
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY,
                title TEXT,
                description TEXT,
                price REAL,
                brand TEXT,
                category TEXT
            )
        ''')


        cursor.execute('''
            INSERT OR REPLACE INTO products (id, title, description, price, brand, category)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (self.id, self.title, self.description, self.price, self.brand, self.category))

        connection.commit()
        connection.close()

response = requests.get('https://dummyjson.com/products')
data = response.json()

for item in data['products']:
    product = Product(
        id=item['id'],
        title=item['title'],
        description=item['description'],
        price=item['price'],
        brand=item['brand'],
        category=item['category']
    )
    product.save()

print("all products database ga saqlandi")
    


