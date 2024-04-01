# Project1-CS325: My News Downloader

## Project Overview

My News Downloader is a Python script designed to automate the downloading of news articles from a list of URLs. It fetches the content of each URL, targeting the news article content while excluding advertisements and other unrelated content. This tool is invaluable for researchers, journalists, and anyone interested in performing content analysis on news articles without the need to manually download each one.

## Features

- **Automated Downloading:** Downloads news articles from a list of URLs provided in a text file named `links.txt`.
- **Content Isolation:** Utilizes BeautifulSoup for HTML parsing to focus on the article content, ignoring ads and navigation.
- **Separate Storage:** Stores each article in a separate text file for easy access and analysis.
- **Simple and Efficient:** Leverages the `requests` library for efficient web requests.

## Prerequisites

- Python 3.x
- Python packages: `beautifulsoup4`, `requests`

Ensure Python and pip are installed on your machine. Python installation instructions can be found at [python.org](https://www.python.org/).

## Installation and Setup

### Clone the Repository

Start by cloning the repository to your local machine:

```sh
git clone https://github.com/StuartLech/Project1-CS325
cd Project1-CS325
```

### Environment Setup

It's recommended to use a virtual environment for Python projects to manage dependencies efficiently.

1. **Create and activate a virtual environment:**

   For macOS/Linux:
   ```sh
   python3 -m venv venv
   source venv/bin/activate
   ```

   For Windows:
   ```sh
   python -m venv venv
   .\venv\Scripts\activate
   ```

2. **Install the required packages:**

   ```sh
   pip install beautifulsoup4 requests
   ```

Alternatively, if you have a `requirements.yml` file, you can initialize the conda environment with:

```sh
conda env create -f requirements.yml
conda activate <env_name>
```

Replace `<env_name>` with the name of your environment as specified in `requirements.yml`.

## Usage

To run the `my_news_downloader.py` script, ensure you're in the project directory and your virtual environment is activated. The script expects a file named `links.txt` in the same directory, containing a list of URLs to news articles, one URL per line.

```sh
python my_news_downloader.py
```

The script will download each article's content, storing them in separate text files within a specified directory.

## Output

Each news article will be saved in a separate text file, named after the article's title or a sequence number, within the `Data` directory (this directory will be created if it does not exist).


