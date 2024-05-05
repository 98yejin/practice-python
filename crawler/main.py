import random
import aiohttp
import asyncio
import urllib.robotparser
from typing import List, Optional, Tuple
from bs4 import BeautifulSoup
from dataclasses import dataclass
from urllib.parse import urlparse


@dataclass
class CrawlResult:
    url: str
    content: Optional[str] = None
    error: Optional[str] = None


class RobotsCache:
    def __init__(self) -> None:
        self.cache = {}

    def can_fetch(self, url, user_agent="*"):
        base_url = self.extract_base_url(url)
        if base_url in self.cache:
            return self.cache[base_url]
        return self.update_cache(base_url, user_agent)

    def update_cache(self, base_url, user_agent):
        parser = urllib.robotparser.RobotFileParser()
        parser.set_url(base_url + "/robots.txt")
        parser.read()
        result = parser.can_fetch(user_agent, base_url)
        self.cache[base_url] = result
        return result

    @staticmethod
    def extract_base_url(url):
        parsed_url = urlparse(url)
        return f"{parsed_url.scheme}://{parsed_url.netloc}"


async def fetch_url(
    session: aiohttp.ClientSession, url: str, delay_range
) -> CrawlResult:
    """
    Fetches the content of a given URL using an asynchronous HTTP session.
    Need to roate User-Agent or use proxy in real world scenario

    Args:
        session (aiohttp.ClientSession): The asynchronous HTTP session.
        url (str): The URL to fetch.
        delay_range: A tuple representing the range of delay in seconds before making the request.

    Returns:
        CrawlResult: An object containing the URL and the fetched content, or an error message if an exception occurs.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0",
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
    cache: RobotsCache, urls: List[str], delay_range: Tuple[int], timeout_seconds: int
) -> List[CrawlResult]:
    filtered_urls = [url for url in urls if cache.can_fetch(url)]
    timeout = aiohttp.ClientTimeout(total=timeout_seconds)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        results = await asyncio.gather(
            *[
                fetch_url(session=session, url=url, delay_range=delay_range)
                for url in filtered_urls
            ]
        )
        return results


async def main(
    urls: List[str], delay_range: Tuple[int], timeout_seconds: int, batch_size: int = 10
):
    cache = RobotsCache()
    batches = [urls[i : i + batch_size] for i in range(0, len(urls), batch_size)]
    return await asyncio.gather(
        *[
            process_batch(cache, batch, delay_range, timeout_seconds)
            for batch in batches
        ]
    )


if __name__ == "__main__":
    urls = [
        "http://example.com/page1",
        "http://example.com/page2",
        "http://example.com/page3",
        # "https://98yejin.github.io",
    ]
    delay_range = (1, 3)
    timeout_seconds = 3
    batch_size = 10
    results = asyncio.run(main(urls, delay_range, timeout_seconds, batch_size))
    print(results)
