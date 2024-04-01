import requests
from bs4 import BeautifulSoup

class ArticleDownloader:
    """Class responsible for downloading articles from URLs.
    
    SRP: This class has the single responsibility of downloading and parsing
    the article content from a given URL.
    """
    
    @staticmethod
    def download_article(url):
        """Download an article given its URL.
        
        Args:
            url (str): The URL of the article to download.
        
        Returns:
            str: The text content of the article, or an error message.
        """
        try:
            response = requests.get(url)
            response.raise_for_status()
            soup = BeautifulSoup(response.content, 'html.parser')
            article = soup.find('article')
            return article.get_text() if article else "Article content not found"
        except requests.RequestException as e:
            return str(e)