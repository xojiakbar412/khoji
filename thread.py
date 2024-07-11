import requests
import sqlite3
import json

response = requests.get("https://dummyjson.com/products")
data = response.json()

products = data['products']

conn = sqlite3.connect('products.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS products (
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
                    weight TEXT)''')

for product in products:
    cursor.execute('''INSERT INTO products (id,
                    title
                    description,
                    price, discountPercentage,
                    rating, stock,
                    brand, category,
                    thumbnail, weight)
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                   (product['id'],
                     product['title'], product['description'], 
                     product['price'],
                    product['discountPercentage'], product['rating'],
                      product['stock'],
                    product['brand'], product['category'],
                      product['thumbnail'], product['weight']))
    
conn.commit()
conn.close()

print('Data saved to database successfully!')