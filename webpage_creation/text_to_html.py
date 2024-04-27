# text_to_html.py
from xml.etree import ElementTree as ET
import os
from pathlib import Path

def txt_to_html(summary_dir, html_output_dir):
    # Ensure the output directory exists
    html_output_dir.mkdir(parents=True, exist_ok=True)
    # Define the path for the output HTML file
    html_file = html_output_dir / "all_news_articles.html"

    # Start building the HTML document
    root = ET.Element("html")
    head = ET.SubElement(root, "head")
    title_element = ET.SubElement(head, "title")
    title_element.text = "News Aggregation"
    body = ET.SubElement(root, "body")

    # Process each text file in the summary directory
    for filename in sorted(os.listdir(summary_dir)):
        if filename.startswith("article_#") and filename.endswith(".txt"):
            file_path = os.path.join(summary_dir, filename)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.readlines()

            # Extract the title and paragraph from the file
            header = content[0].strip()
            paragraph = "".join(content[1:]).strip()

            # Add the title and paragraph to the HTML body
            h1 = ET.SubElement(body, "h1")
            h1.text = header
            p = ET.SubElement(body, "p")
            p.text = paragraph

    # Write the constructed HTML to the specified file
    tree = ET.ElementTree(root)
    tree.write(html_file, encoding='utf-8', xml_declaration=True)

    return html_file

