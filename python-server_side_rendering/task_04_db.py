#!/usr/bin/env python3
from flask import Flask, render_template, request
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/items')
def items():
    with open('items.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    items_list = data.get('items', [])
    return render_template('items.html', items=items_list)


def read_json_file():
    """Read and return data from products.json file"""
    try:
        with open('products.json', 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        return None
    except json.JSONDecodeError:
        return None


def read_csv_file():
    """Read and return data from products.csv file"""
    try:
        products = []
        with open('products.csv', 'r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                products.append({
                    'id': int(row['id']),
                    'name': row['name'],
                    'category': row['category'],
                    'price': float(row['price'])
                })
        return products
    except FileNotFoundError:
        return None
    except (ValueError, KeyError):
        return None


def read_sql_database():
    """Read and return data from SQLite database"""
    try:
        conn = sqlite3.connect('products.db')
        cursor = conn.cursor()
        cursor.execute('SELECT id, name, category, price FROM Products')
        rows = cursor.fetchall()
        conn.close()
        
        products = []
        for row in rows:
            products.append({
                'id': row[0],
                'name': row[1],
                'category': row[2],
                'price': row[3]
            })
        return products
    except sqlite3.Error:
        return None


@app.route('/products')
def products():
    """Display products from JSON, CSV, or SQL based on source parameter"""
    source = request.args.get('source')
    product_id = request.args.get('id')
    
    # Validate source parameter
    if source not in ['json', 'csv', 'sql']:
        return render_template('product_display.html', 
                             error="Wrong source")
    
    # Read data from appropriate source
    if source == 'json':
        products_data = read_json_file()
    elif source == 'csv':
        products_data = read_csv_file()
    else:  # sql
        products_data = read_sql_database()
    
    # Check if file/database reading was successful
    if products_data is None:
        return render_template('product_display.html', 
                             error="Error reading data source")
    
    # Filter by ID if provided
    if product_id:
        try:
            product_id = int(product_id)
            filtered_products = [p for p in products_data if p['id'] == product_id]
            if not filtered_products:
                return render_template('product_display.html', 
                                     error="Product not found")
            products_data = filtered_products
        except ValueError:
            return render_template('product_display.html', 
                                 error="Invalid product ID")
    
    return render_template('product_display.html', 
                         products=products_data)


if __name__ == '__main__':
    app.run(debug=True, port=5000)
