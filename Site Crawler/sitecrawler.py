import requests
from bs4 import BeautifulSoup
import csv
from urllib.parse import urlparse, urljoin
import signal

# Predefined list of websites for the user to choose from
websites = {
    '1': {'name': 'HTTPBin', 'url': 'http://httpbin.org/'},
    '2': {'name': 'Books to Scrape', 'url': 'http://books.toscrape.com/'},
    '3': {'name': 'Quotes to Scrape', 'url': 'http://quotes.toscrape.com/'}
}

crawled_urls = set()
urls_to_crawl = []

def get_links(url):
    domain = urlparse(url).netloc
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for link in soup.find_all('a', href=True):
            absolute_link = urljoin(url, link['href'])
            if urlparse(absolute_link).netloc == domain and absolute_link not in crawled_urls:
                yield absolute_link
    except requests.exceptions.RequestException:
        pass

def crawl(start_url, max_depth=3):
    urls_to_crawl.append((start_url, 0))
    while urls_to_crawl:
        url, depth = urls_to_crawl.pop(0)
        if depth > max_depth:
            continue
        if url not in crawled_urls:
            print(f"Crawling: {url} (Remaining: {len(urls_to_crawl)} / Crawled: {len(crawled_urls)})")
            crawled_urls.add(url)
            if depth < max_depth:
                for link in get_links(url):
                    urls_to_crawl.append((link, depth + 1))

def signal_handler(signal, frame):
    print('\nProcess interrupted by user. Saving crawled URLs...')
    save_crawled_urls()
    print('Crawled URLs have been saved. Exiting now.')
    exit(0)

def save_crawled_urls():
    with open('crawled_urls.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        for url in crawled_urls:
            writer.writerow([url])

def main():
    signal.signal(signal.SIGINT, signal_handler)
    print("Please choose a website to crawl:")
    for key, value in websites.items():
        print(f"{key}: {value['name']}")
    choice = input("Enter the number of the website you want to crawl: ")

    if choice in websites:
        start_url = websites[choice]['url']
        print(f"Starting crawl at {start_url}. Press Ctrl+C to stop.")
        crawl(start_url)
    else:
        print("Invalid choice. Exiting.")
        return  # Ensure exiting before saving

    save_crawled_urls()  # Save after crawling if not interrupted
    print(f'Crawled URLs have been written to "crawled_urls.csv".')

if __name__ == "__main__":
    main()
