import requests
import sqlite3
import threading  

def create_db():
    conn = sqlite3.connect('products.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS products (
        id INTEGER PRIMARY KEY,
        title TEXT,
        description TEXT,
        price REAL,
        discountPercentage REAL,
        rating REAL,
        stock INTEGER,
        brand TEXT,
        category TEXT,
        thumbnail TEXT,
        images TEXT,
        weight TEXT
    )
    ''')
    conn.commit()
    conn.close()

def save_to_db(product):
    conn = sqlite3.connect('product.db')
    c = conn.cursor()
    c.execute('''
    INSERT INTO products (id, title, description, price, discountPercentage, rating, stock, brand, category, thumbnail, images, weight)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        product['id'], product['title'], product['description'], product['price'], product['discountPercentage'], product['rating'], product['stock'], product['brand'], product['category'], product['thumbnail'], ','.join(product['images']), product.get('weight', 'N/A')
    ))
    
    conn.commit()
    conn.close()

def fetch_and_save_products():
    response = requests.get('https://dummyjson.com/products')
    if response.status_code == 200:
        products = response.json().get('products', [])
        for product in products:
            save_to_db(product)

def main():
    create_db()
    thread = threading.Thread(target=fetch_and_save_products)
    thread.start()
    thread.join()

if __name__ == '__main__':
    main()
