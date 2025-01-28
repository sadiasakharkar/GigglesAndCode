import requests
from bs4 import BeautifulSoup

# URL to be scraped
url = 'https://www.docdroid.net/Incp3Kq/rich-dad-poor-dad-pdf'

# Send a request to fetch the page content
response = requests.get(url)

# Parse the page content with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find the download link based on the HTML structure
download_link = soup.find('a', class_='downloadLink')['href']

# Print the download link
print("Download link:", download_link)
