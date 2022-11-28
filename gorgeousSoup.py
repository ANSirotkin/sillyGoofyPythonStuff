import requests
from bs4 import BeautifulSoup

response = requests.get("https://cnn.com/")
if response.status_code != 200:
	print("Error fetching page")
	exit()
else:
	content = response.text

soup = BeautifulSoup(response.content, 'html.parser')

print(soup.prettify())