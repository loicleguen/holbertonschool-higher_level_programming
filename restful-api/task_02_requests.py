#!/usr/bin/python3
import requests
import json
import csv


def fetch_and_print_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post.get('title'))


def fetch_and_save_posts():
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    
    if response.status_code == 200:
        posts_data = response.json()
        structured_data = []
        for post in posts_data:
            structured_data.append({
                'id': post.get('id'),
                'title': post.get('title'),
                'body': post.get('body')
            })

        with open('posts.csv', 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, ['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(structured_data)
        
        return True
    else:
        print(f"Request error : {response.status_code}")
        return False
