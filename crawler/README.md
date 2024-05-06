# Asynchronous Web Crawler

## Overview

This Python script defines an asynchronous web crawler that efficiently retrieves and processes web content using the aiohttp library. The crawler supports configurable concurrency levels, user-agent rotation, and error handling with retries. It is suitable for tasks such as data scraping, site monitoring, or content aggregation.

## Features

- Asynchronous Crawling: Utilizes asyncio and aiohttp for non-blocking I/O operations.
- Error Handling: Implements retry logic with exponential backoff using tenacity.
- User-Agent Rotation: Rotates user agents on each request to avoid blocking.
- Delay Between Requests: Configurable random delays between requests to mimic human interaction and reduce server load impact.
- Configurable Batch Processing: Supports crawling URLs in batches to manage large sets of URLs efficiently.
- Content Extraction: Uses BeautifulSoup to parse HTML and extract text content.

## Requirements

Python 3.7 or higher
aiohttp
BeautifulSoup4
tenacity
Install the required Python packages using pip:

```bash
pip install -r requirements.txt
```

## Configuration

Configuration for the crawler is defined in a JSON file (config.json). The configuration includes:

- urls: List of URLs to crawl.
- delay_range: Tuple indicating the range (in seconds) to wait between requests.
- timeout_seconds: Timeout for each HTTP request.
- user_agents: List of user agent strings to use for requests.
- batch_size: Number of URLs to process in each batch.

Example of config.json:

```json
{
  "urls": ["http://example.com", "http://example.org"],
  "delay_range": [1, 3],
  "timeout_seconds": 30,
  "batch_size": 10,
  "user_agents": [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
  ]
}
```

## Usage

Set Up Configuration: Modify config.json with your desired settings.

## Output

The script outputs a list of CrawlResult objects, each containing:

- url: URL of the fetched page.
- content: Extracted text content from the page (if successful).
- error: Error message (if an error occurred).
