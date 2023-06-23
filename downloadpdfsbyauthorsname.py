import requests
from bs4 import BeautifulSoup

# Function to extract ArXiv PDF links from a webpage
def extract_arxiv_pdf_links(url):
	response = requests.get(url)
	soup = BeautifulSoup(response.content, 'html.parser')
	pdf_links = []

	# Find all the anchor tags
	anchors = soup.find_all('a')
    
	# Extract ArXiv PDF links
	for anchor in anchors:
    	href = anchor.get('href')
    	if href and 'arxiv.org/pdf' in href:
        	pdf_links.append(href)
	return pdf_links

# Example usage
query = input("Nome do autor: ")
query = query.replace(' ','+')
url = f'https://arxiv.org/search/?query={query}&searchtype=all'
pdf_links = extract_arxiv_pdf_links(url)

# Print all the ArXiv PDF links
for link in pdf_links:
	response = requests.get(link)
	filename = link.split('/')[-1] + '.pdf'
	with open(filename, 'wb') as file:
    	file.write(response.content)
	print(f"Downloaded: {filename}")
