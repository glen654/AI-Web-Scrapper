# AI Web Scraper with Streamlit and Langchain

This project implements an AI-powered web scraper using the following technologies:

1.**Streamlit:** For creating the web interface to interact with the AI-powered scraper.

2.**Langchain:** For integrating language models and chain-of-thought reasoning to interpret and extract relevant data from the web pages.

3.**Langchain_ollama:** An integration with Ollama models to provide natural language understanding and processing.

4.**Selenium: **To automate web browser interaction for dynamic content loading.

5.**BeautifulSoup4:** For parsing and extracting data from HTML documents.

6.**Lxml:** For efficient HTML and XML parsing.

7.**Html5lib:** An additional HTML parser for more lenient parsing when required.

8.**python-dotenv:** For managing environment variables securely.


## Project Overview

This project allows users to input a website URL and specify the data they want to scrape. The scraper will navigate the webpage, extract the relevant content, and provide it to the user. This tool leverages the power of AI to intelligently interpret the content and help users find exactly what they need from any given web page.

## Features

**Interactive Web Interface:** Built with Streamlit to easily enter URLs and customize scraping tasks.

**AI-Enhanced Scraping:** Uses Langchain and Langchain_ollama to interpret natural language queries and process web page content more intelligently.

**Browser Automation:** Selenium is used for automating browser interactions with dynamic pages, ensuring content is fully loaded before extraction.

**Data Extraction:** Scrapes and extracts structured data from the web using BeautifulSoup4, Lxml, and Html5lib for reliable HTML parsing.

**Environment Configuration:** .env file handling for managing sensitive information like API keys and credentials.


## Installation

### Prerequisites

Make sure you have Python 3.7+ installed on your machine. You will also need to install the required dependencies for this project.

### Steps

1.Clone the repository:

`git clone https://github.com/your-username/ai-web-scraper.git`

`cd ai-web-scraper`


2.Install required Python packages:

`pip install -r requirements.txt`

3.Create a .env file and add any necessary environment variables such as API keys, URLs, etc.

4.Run the application:

`streamlit run app.py`

## How It Works

**Input URL:** The user enters a URL of the page they want to scrape.

**Define Task:** The user specifies what type of data they are looking for (e.g., product names, prices, news headlines).

**AI Interpretation:** Langchain processes the user's request and intelligently identifies relevant content from the page, using Langchain_ollama to assist in language understanding.

**Web Scraping:** Selenium is used to interact with the webpage, ensuring that all dynamic content is loaded before scraping.

**Data Extraction:** BeautifulSoup4 and Lxml parse the HTML to extract the required data in a structured format.

**Display Results:** The extracted data is displayed in the Streamlit interface for the user to view or download.


## Dependencies

The following libraries are required for the scraper to function:

`streamlit:` For building the web interface.

`langchain:` For creating and using AI chains to process web data.

`langchain_ollama:` To integrate with Ollama models for enhanced AI processing.

`selenium:` For automating browser interactions with dynamic pages.

`beautifulsoup4:` For parsing HTML and extracting data.

`lxml:` An efficient parser for HTML and XML.

`html5lib:` A lenient HTML parser.

`python-dotenv:` For managing environment variables.


## Usage

1.Launch the app using streamlit run app.py.

2.Enter the URL of the website you want to scrape.

3.Provide a natural language description of the data you want to extract.

4.Review the results displayed in the app interface.


## Contributing

Feel free to fork this repository and create a pull request if you would like to contribute. Please make sure to follow the coding style and write tests for any new features you add.