import requests
from bs4 import BeautifulSoup
import csv
import json
import os
import re
import urllib.request  # Added for image downloading

# Function to check if the CSV file is open elsewhere
def is_csv_file_open(file_path):
    try:
        # Try to open the file in 'append' mode to test if it's open elsewhere
        with open(file_path, 'a', newline='', encoding='utf-8-sig'):
            pass
        return False  # If successful, file is not open elsewhere
    except IOError:
        return True  # If an error occurs, file is open elsewhere

# Main function to perform scraping
def main():
    script_dir = os.path.dirname(os.path.realpath(__file__))  # Get directory of the script
    config_file_path = os.path.join(script_dir, 'config.json')  # Full path to configuration file

    # Check if the configuration file exists
    if not os.path.exists(config_file_path):
        print(f"Configuration file not found: {config_file_path}")
        return  # Exit if configuration file doesn't exist

    # Load the JSON configuration for websites
    with open(config_file_path, 'r') as config_file:
        config = json.load(config_file)  # Load configuration from JSON

    # Prepare the URL validation pattern
    url_pattern = re.compile(r'https://books.toscrape.com/catalogue/.+/index.html')

    # Path to save the CSV file
    csv_file_path = os.path.join(script_dir, 'book_details.csv')  # CSV file path

    # Check if the CSV file is currently open
    while is_csv_file_open(csv_file_path):
        input("Please close the CSV file and then press Enter to continue...")

    while True:  # Loop to allow multiple scraping sessions
        urls_input = input("Enter the list of book URLs to scrape from books.toscrape.com, separated by spaces (or type 'quit' to exit): ").strip()
        if urls_input.lower() == 'quit':
            break  # User chose to exit

        urls = urls_input.split()  # Split input into list of URLs

        if urls:
            with open(csv_file_path, 'w', newline='', encoding='utf-8-sig') as file:
                writer = csv.writer(file)
                # Updated to include 'Image Path' in the CSV header
                writer.writerow(['Title', 'Price (excl. tax)', 'Price (incl. tax)', 'Availability', 'Description', 'UPC', 'Product Type', 'Tax', 'Number of Reviews', 'Image Path'])

                for url in urls:  # Process each provided URL
                    if url_pattern.match(url):
                        response = requests.get(url)
                        response.encoding = 'utf-8'  # Ensure correct encoding
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.content, 'html.parser')

                            # Extract book details using BeautifulSoup based on typical structure
                            title = soup.find('h1').get_text().strip() if soup.find('h1') else 'N/A'
                            availability = soup.find('p', class_='instock availability').get_text().strip() if soup.find('p', class_='instock availability') else 'N/A'
                            description_tag = soup.find(id='product_description')
                            description = description_tag.find_next_sibling('p').get_text().strip() if description_tag else 'N/A'
                            
                            # Extracting details from the product table
                            product_info = {row.th.text.strip(): row.td.text.strip() for row in soup.find('table', class_='table table-striped').find_all('tr')}
                            upc = product_info.get('UPC', 'N/A')
                            product_type = product_info.get('Product Type', 'N/A')
                            price_excl_tax = product_info.get('Price (excl. tax)', 'N/A')
                            price_incl_tax = product_info.get('Price (incl. tax)', 'N/A')
                            tax = product_info.get('Tax', 'N/A')
                            number_of_reviews = product_info.get('Number of reviews', 'N/A')

                            # New section: image downloading
                            image_container = soup.select_one(config["books.toscrape.com"]["image_selector"])
                            image_path = 'N/A'  # Default if no image found
                            if image_container:
                                image_relative_url = image_container.get('src')
                                image_absolute_url = urllib.parse.urljoin(url, image_relative_url)
                                image_filename = f"{title.replace('/', '|')}.jpg"  # Replace slashes with vertical bars
                                image_path = os.path.join(script_dir, 'images', image_filename)
                                os.makedirs(os.path.join(script_dir, 'images'), exist_ok=True)  # Ensure the 'images' directory exists
                                urllib.request.urlretrieve(image_absolute_url, image_path)

                            # Write all extracted details to the CSV
                            writer.writerow([title, price_excl_tax, price_incl_tax, availability, description, upc, product_type, tax, number_of_reviews, image_path])
                            print(f"Completed scraping data for: {url}")
                        else:
                            print(f"Failed to fetch {url} with status code {response.status_code}")
                    else:
                        print(f"URL does not match required pattern: {url}")

            print(f"Data from {len(urls)} URLs has been written to '{csv_file_path}'.")  # Notify completion

        continue_scraping = input("Do you want to scrape more URLs? (yes/no): ").strip().lower()
        if continue_scraping != 'yes':
            break  # Exit loop if user does not want to continue

if __name__ == "__main__":
    main()
