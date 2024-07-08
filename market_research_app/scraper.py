import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Extract relevant data
    # Example: headlines = [h.text for h in soup.find_all('h1')]
    return soup
