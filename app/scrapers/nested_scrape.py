import requests
from bs4 import BeautifulSoup
import time
import os


def get_html(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error while fetching the URL: {e}")
        return None


def save_to_file(content, file_path, filename):
    if not os.path.exists(file_path):
        os.makedirs(file_path)
    with open(os.path.join(file_path, filename), "a", encoding="utf-8") as file:
        file.write(content)

# ---= These function need to be implemented and will be different for each forum =---
# ---- In order to make this scraper work on any forum, there will be a pre-processing step
# ---- that will generate a map of the forum's structure and export it as a CSV file and a JSON file.
# def extract_subcategory_links(html):
#     # Implement this function based on the forum's structure
#     pass


# def extract_thread_links(html):
#     # Implement this function based on the forum's structure
#     pass


# def extract_post_links(html):
#     # Implement this function based on the forum's structure
#     pass


# def extract_post_data(html):
#     # Implement this function based on the forum's structure
#     pass


def scrape_forum(base_url, file_path, filename, delay=1):
    html = get_html(base_url)
    if html is None:
        print("Failed to fetch the base URL.")
        return

    for subcategory_url in extract_subcategory_links(html):
        subcategory_html = get_html(subcategory_url)
        time.sleep(delay)

        for thread_url in extract_thread_links(subcategory_html):
            thread_html = get_html(thread_url)
            time.sleep(delay)

            for post_url in extract_post_links(thread_html):
                post_html = get_html(post_url)
                time.sleep(delay)

                post_data = extract_post_data(post_html)
                save_to_file(post_data, file_path, filename)


if __name__ == "__main__":
    forum_url = "https://forums.nexusmods.com/index.php?/forum/20-morrowind-discussion/"  # Replace with the forum's URL
    file_path = input(
        "Enter the location to create the 'modvis_scrapes' folder: ").strip()
    file_path = os.path.join(file_path, "modvis_scrapes")
    filename = input("Enter the name of the output .txt file: ").strip()
    scrape_forum(forum_url, file_path, filename)
