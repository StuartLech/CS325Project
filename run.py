from module_1.some_name1 import ArticleDownloader
from module_2.some_name2 import FileManager

def main():
    """The main function to run the article downloader program.
    
    It reads URLs from a file, downloads the articles, and writes them to
    another file in the processed directory.
    """
    input_file = 'Data/raw/links.txt'
    output_prefix = 'Data/processed/article_#'
    
    urls = FileManager.read_urls_from_file(input_file)
    
    for i, url in enumerate(urls, start=1):
        content = ArticleDownloader.download_article(url.strip())
        output_file = f'{output_prefix}{i}.txt'
        FileManager.write_content_to_file(content, output_file)

if __name__ == '__main__':
    main()
