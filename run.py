# run.py
from module_1.some_name1 import ArticleDownloader
from module_2.some_name2 import FileManager
from module_3.some_name3 import ArticleSummarizer
from webpage_creation.text_to_html import txt_to_html
from pathlib import Path

def main():
    # Read URLs from the input file
    input_file = 'Data/raw/links.txt'
    urls = FileManager.read_urls_from_file(input_file)
    
    # Initialize the summarizer
    summarizer = ArticleSummarizer()

    # Process each URL to download and summarize content
    for i, url in enumerate(urls, start=1):
        # Download the article
        content = ArticleDownloader.download_article(url.strip())
        
        # Save the downloaded content to a file
        raw_output_file = f'Data/processed/article_#{i}.txt'
        FileManager.write_content_to_file(content, raw_output_file)
        
        # Summarize the article and save the summarized content
        title, summarized_content = summarizer.summarize_article(content)
        summarized_output_file = f'Data/summarized/article_#{i}.txt'
        FileManager.write_content_to_file(f"Title: {title}\n\n{summarized_content}", summarized_output_file)

    # Define the paths for the summary and HTML output directories
    summary_dir = Path("Data/summarized")
    html_output_dir = Path("webpage_creation")  # Changed to 
    txt_to_html(summary_dir, html_output_dir)

if __name__ == '__main__':
    main()
