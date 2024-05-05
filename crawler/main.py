import json
import random
import aiohttp
import asyncio
from typing import List, Optional, Tuple
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class CrawlResult:
    url: str
    content: Optional[str] = None
    error: Optional[str] = None


@dataclass
class Config:
    urls: List[str]
    delay_range: Tuple[int, int]
    timeout_seconds: int
    batch_size: Optional[int] = 10


USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
    "Mozilla/5.0 (iPad; CPU OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1",
]


async def fetch_url(
    session: aiohttp.ClientSession, url: str, delay_range
) -> CrawlResult:
    """
    Fetches the content of a given URL using an asynchronous HTTP session.
    Need to rotate User-Agent or use proxy in real-world scenarios.

    Args:
        session (aiohttp.ClientSession): The asynchronous HTTP session.
        url (str): The URL to fetch.
        delay_range (tuple): A tuple representing the range of delay in seconds before making the request.

    Returns:
        CrawlResult: An object containing the URL and the fetched content, or an error message if an exception occurs.
    """
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        "Accept": "*/*",
    }
    try:
        await asyncio.sleep(random.uniform(*delay_range))
        async with session.get(url, headers=headers, allow_redirects=True) as response:
            response.raise_for_status()
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            text = soup.getText(separator="\n", strip=True)
            return CrawlResult(url=url, content=text)
    except Exception as e:
        print(f"[ERROR] {type(e).__name__}: {e}")
        return CrawlResult(url=url, error=str(e))


async def process_batch(
    urls: List[str], delay_range: Tuple[int], timeout_seconds: int
) -> List[CrawlResult]:
    """
    Process a batch of URLs asynchronously.

    Args:
        urls (List[str]): List of URLs to crawl.
        delay_range (Tuple[int]): Range of delay in seconds between each request.
        timeout_seconds (int): Timeout in seconds for each request.

    Returns:
        List[CrawlResult]: List of crawl results.

    """
    timeout = aiohttp.ClientTimeout(total=timeout_seconds)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        results = await asyncio.gather(
            *[
                fetch_url(session=session, url=url, delay_range=delay_range)
                for url in urls
            ]
        )
        return results


async def main(config: Config):
    """
    Executes the main crawling process.

    Args:
        config (Config): The configuration object containing the URLs, batch size, delay range, and timeout.

    Returns:
        List[Result]: A list of results from processing each batch of URLs.
    """
    urls = config.urls
    batches = [
        urls[i : i + config.batch_size] for i in range(0, len(urls), config.batch_size)
    ]
    return await asyncio.gather(
        *[
            process_batch(batch, config.delay_range, config.timeout_seconds)
            for batch in batches
        ]
    )


if __name__ == "__main__":
    with open("config.json", "r") as file:
        data = json.load(file)
    config = Config(
        urls=data["urls"],
        delay_range=tuple(data["delay_range"]),  # Convert list to tuple
        timeout_seconds=data["timeout_seconds"],
        batch_size=data["batch_size"],
    )
    results = asyncio.run(main(config))
    print(results)
