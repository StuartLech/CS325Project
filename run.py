from module_1.some_name1 import ArticleDownloader
from module_2.some_name2 import FileManager
from module_3.some_name3 import ArticleSummarizer

def main():
    """The main function to run the article downloader program.
    
    It reads URLs from a file, downloads the articles, and writes them to
    another file in the processed directory.
    """
    input_file = 'Data/raw/links.txt'
    raw_output_prefix = 'Data/processed/article_#'
    summarized_output_prefix = 'Data/summarized/article_#'
    
    urls = FileManager.read_urls_from_file(input_file)
    summarizer = ArticleSummarizer()

    for i, url in enumerate(urls, start=1):
        # Download and save the raw article content
        content = ArticleDownloader.download_article(url.strip())
        raw_output_file = f'{raw_output_prefix}{i}.txt'
        FileManager.write_content_to_file(content, raw_output_file)
        
        # Summarize content and handle titles
        title, summarized_content = summarizer.summarize_article(content)
        summarized_output_file = f'{summarized_output_prefix}{i}.txt'
        summarized_content_with_title = f"Title: {title}\n\n{summarized_content}"
        FileManager.write_content_to_file(summarized_content_with_title, summarized_output_file)

if __name__ == '__main__':
    main()
