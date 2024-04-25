# Example debug statements in run.py
print("Starting the main function")

from module_1.some_name1 import ArticleDownloader
from module_2.some_name2 import FileManager
from module_3.some_name3 import ArticleSummarizer
from webpage_creation.text_to_html import txt_to_html
from pathlib import Path

def main():
    print("Reading URL file")
    input_file = 'Data/raw/links.txt'
    urls = FileManager.read_urls_from_file(input_file)
    
    print(f"Found {len(urls)} URLs to process.")
    summarizer = ArticleSummarizer()

    for i, url in enumerate(urls, start=1):
        print(f"Processing URL {i}: {url}")
        content = ArticleDownloader.download_article(url.strip())
        print(f"Downloaded content for URL {i}")
        
        raw_output_file = f'Data/processed/article_#{i}.txt'
        FileManager.write_content_to_file(content, raw_output_file)
        
        title, summarized_content = summarizer.summarize_article(content)
        summarized_output_file = f'Data/summarized/article_#{i}.txt'
        FileManager.write_content_to_file(f"Title: {title}\n\n{summarized_content}", summarized_output_file)

    print("Generating HTML from summaries")
    summary_dir = Path("Data/summarized")
    html_output_dir = Path("Data/HTML")
    txt_to_html(summary_dir, html_output_dir)

if __name__ == '__main__':
    main()
    print("Finished processing all articles")
