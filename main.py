import requests
from bs4 import BeautifulSoup

def main():

    print("Iniciando implementação de WebScraping")
    url = 'https://www.linkedin.com/feed/'
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    
    data = soup.find_all("p")

    for item in data:
        print(item.text) 

main()