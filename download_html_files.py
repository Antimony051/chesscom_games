import requests
import time
import os
from typing import List

# Base URL for downloading chess game pages
BASE_URL = "https://www.chess.com/games/archive?page={page}"

# HTTP headers for the request
HEADERS = {
    "Host": "www.chess.com",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.5",
    "Accept-Encoding": "gzip, deflate, br, zstd",
    "DNT": "1",
    "Sec-GPC": "1",
    "Connection": "keep-alive",
    "Referer": "https://www.chess.com/games/archive?gameType=recent&gameTypeslive%5B0%5D=rapid&gameOwner=my_game&page=1",
    "Cookie": "<your_cookie_here>",  # Replace with your actual cookie (you can get this from your browser)
    "Upgrade-Insecure-Requests": "1",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Priority": "u=0, i"
}

def download_page(output_dir: str, page: int) -> bool:
    """
    Downloads a chess game archive page and saves it as a file.

    Args:
        output_dir (str): Directory to save the downloaded page.
        page (int): Page number to download.

    Returns:
        bool: True if the page was successfully downloaded, False otherwise.
    """
    print(f"Downloading page {page}...")

    url = BASE_URL.format(page=page)

    #Check if the 'Cookie' header is set
    if not HEADERS["Cookie"] or "<your_cookie_here>" in HEADERS["Cookie"]:
        print("Please set the 'Cookie' header in the HEADERS dictionary.")
        return False
    
    try:
        response = requests.get(url, headers=HEADERS)

        if response.status_code == 429:
            print("Rate limited! Sleeping for 30 seconds...")
            time.sleep(30)
            return download_page(output_dir, page)

        if response.status_code != 200:
            print(f"Failed to download page {page}. Status code: {response.status_code}")
            return False

        # Save the response content
        file_path = os.path.join(output_dir, f"page_{page}.html")
        with open(file_path, "wb") as f:
            f.write(response.content)

        return True

    except requests.RequestException as e:
        print(f"Error downloading page {page}: {e}")
        return False

def find_missing_pages(directory: str, total_pages: int = 101) -> List[int]:
    """
    Identifies which pages are missing from the directory.

    Args:
        directory (str): Path to the directory containing saved pages.
        total_pages (int): Total number of pages in your game history (go to https://www.chess.com/games/archive and click last to see).

    Returns:
        List[int]: A list of missing page numbers.
    """
    existing_files = set(os.listdir(directory))
    missing_pages = [
        i for i in range(1, total_pages + 1) if f"page_{i}.bin" not in existing_files
    ]
    return missing_pages

def main():
    # Define paths (modify as needed before running)
    OUTPUT_DIRECTORY = "path/to/your/games/folder"

    os.makedirs(OUTPUT_DIRECTORY, exist_ok=True)

    # Find missing pages (for the first run all the pages should be missing)
    missing_pages = find_missing_pages(OUTPUT_DIRECTORY)

    if not missing_pages:
        print("All pages are already downloaded. No action needed.")
        return

    # Download missing pages
    for page in missing_pages:
        if download_page(OUTPUT_DIRECTORY, page):
            print(f"Successfully downloaded page {page}.")
        else:
            print(f"Failed to download page {page}.")

if __name__ == "__main__":
    main()
