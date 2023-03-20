import requests
from bs4 import BeautifulSoup
import csv
import os

def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching the URL: {e}")
        return None

def analyze_forum_structure(html):
    # Implement this function based on the forum's structure
    # Example structure: {'subcategory': {'thread': ['post1', 'post2', ...]}}
    forum_structure = {}
    return forum_structure

def flatten_structure(forum_structure):
    flat_structure = []
    for subcategory, threads in forum_structure.items():
        for thread, posts in threads.items():
            for post in posts:
                flat_structure.append({'subcategory': subcategory, 'thread': thread, 'post': post})
    return flat_structure

def save_structure_to_csv(flat_structure, file_path, filename):
    if not os.path.exists(file_path):
        os.makedirs(file_path)

    csv_file = os.path.join(file_path, filename)
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        fieldnames = ['subcategory', 'thread', 'post']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in flat_structure:
            writer.writerow(row)

def main():
    forum_url = input("Enter the forum URL to analyze: ").strip()
    html = get_html(forum_url)
    if html is None:
        print("Failed to fetch the forum URL.")
        return

    forum_structure = analyze_forum_structure(html)
    flat_structure = flatten_structure(forum_structure)

    file_path = input("Enter the location to save the CSV file: ").strip()
    filename = input("Enter the name for the CSV file: ").strip()
    save_structure_to_csv(flat_structure, file_path, filename)
    print(f"CSV file saved to {os.path.join(file_path, filename)}")

if __name__ == "__main__":
    main()
