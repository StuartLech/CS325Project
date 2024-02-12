import requests
from bs4 import BeautifulSoup

def download_article(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  
        soup = BeautifulSoup(response.content, 'html.parser')
        article = soup.find('article')
        return article.get_text() if article else "Article content not found"
    except requests.RequestException as e:
        return str(e)

def main():
    input_file = 'links.txt'
    output_prefix = 'article_'
    
    with open(input_file, 'r') as file:
        urls = file.readlines()
    
    for i, url in enumerate(urls, start=1):
        content = download_article(url.strip())
        with open(f'{output_prefix}{i}.txt', 'w') as outfile:
            outfile.write(content)

if __name__ == '__main__':
    main()
