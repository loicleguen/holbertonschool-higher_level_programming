#!/usr/bin/python3
import requests
import csv
import json

def fetch_and_print_posts():
    """Fetches posts from JSONPlaceholder and prints the titles."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        posts = response.json()
        for post in posts:
            print(post["title"])
        else:
            print("Erreur lors de la récupération des posts.")

def fetch_and_save_posts():
    """Fetches posts from JSONPlaceholder and saves them into a CSV file."""
    url = "https://jsonplaceholder.typicode.com/posts"
    response = requests.get(url)
    if response.status_code == 200:
        posts = response.json()
        data = [
            {"id": post["id"], "title": post["title"], "body": post["body"]}
            for post in posts
        ]

        with open("posts.csv", mode="w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(data)
        print("Les posts ont été enregistrés dans posts.csv ✅")
    else:
        print("Erreur lors de la récupération des posts.")