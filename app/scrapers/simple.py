import requests
from bs4 import BeautifulSoup
import os


def get_page_content(url):
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
    with open(os.path.join(file_path, filename), "w", encoding="utf-8") as file:
        file.write(content)


def main():
    url = input("Enter the URL to scrape: ").strip()

    content = get_page_content(url)
    if content is None:
        print("Failed to scrape the URL.")
        return

    soup = BeautifulSoup(content, "html.parser")
    text_content = soup.get_text()

    file_path = input(
        "Enter the location to create the 'modvis_scrapes' folder: ").strip()
    file_path = os.path.join(file_path, "modvis_scrapes")
    filename = input("Enter the name of the output .txt file: ").strip()

    save_to_file(text_content, file_path, filename)
    print(f"Content saved to {os.path.join(file_path, filename)}")


if __name__ == "__main__":
    main()
