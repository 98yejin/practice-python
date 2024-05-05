import json
import random
import aiohttp
import asyncio
from typing import List, Optional, Tuple
from bs4 import BeautifulSoup
from dataclasses import dataclass
from tenacity import (
    retry,
    wait_exponential,
    stop_after_attempt,
)


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
    user_agents: List[str]
    batch_size: Optional[int] = 10


@retry(wait=wait_exponential(multiplier=1, min=4, max=10), stop=stop_after_attempt(5))
async def make_request(session: aiohttp.ClientSession, url: str, headers: dict):
    async with session.get(url, headers=headers, allow_redirects=True) as response:
        try:
            response.raise_for_status()
        except Exception as e:
            print(f"[ERROR] {type(e).__name__}: {e}")
            raise e
        return await response.text()


class Crawler:
    def __init__(self, config: Config) -> None:
        self.config = config

    async def fetch_url(self, session: aiohttp.ClientSession, url: str) -> CrawlResult:
        """
        Fetches the content of a given URL using an asynchronous HTTP session.
        Need to rotate User-Agent or use proxy in real-world scenarios.

        Args:
            session (aiohttp.ClientSession): The asynchronous HTTP session.
            url (str): The URL to fetch.

        Returns:
            CrawlResult: An object containing the URL and the fetched content, or an error message if an exception occurs.
        """
        headers = {
            "User-Agent": random.choice(self.config.user_agents),
            "Accept": "*/*",
        }
        try:
            await asyncio.sleep(random.uniform(*self.config.delay_range))
            html = await make_request(session, url, headers)
            soup = BeautifulSoup(html, "html.parser")
            text = soup.getText(separator="\n", strip=True)
            return CrawlResult(url=url, content=text)
        except Exception as e:
            print(f"[ERROR] {type(e).__name__}: {e}")
            return CrawlResult(url=url, error=str(e))

    async def process_batch(
        self, session: aiohttp.ClientSession, urls: List[str]
    ) -> List[CrawlResult]:
        """
        Process a batch of URLs asynchronously.

        Args:
            session (aiohttp.ClientSession): The asynchronous HTTP session.
            urls (List[str]): List of URLs to crawl.

        Returns:
            List[CrawlResult]: List of crawl results.

        """
        results = await asyncio.gather(
            *[self.fetch_url(session=session, url=url) for url in urls]
        )
        return results

    async def run(self):
        """
        Executes the run crawling process.

        Args:
            config (Config): The configuration object containing the URLs, batch size, delay range, and timeout.

        Returns:
            List[Result]: A list of results from processing each batch of URLs.
        """
        urls = self.config.urls
        batches = [
            urls[i : i + self.config.batch_size]
            for i in range(0, len(urls), self.config.batch_size)
        ]
        timeout = aiohttp.ClientTimeout(total=self.config.timeout_seconds)
        async with aiohttp.ClientSession(timeout=timeout) as session:
            return await asyncio.gather(
                *[self.process_batch(session, batch) for batch in batches]
            )


def get_unique_urls(urls: List[str]) -> List[str]:
    return list(set(urls))


if __name__ == "__main__":
    with open("config.json", "r") as file:
        data = json.load(file)
    unique_urls = get_unique_urls(data["urls"])
    config = Config(
        urls=unique_urls,
        delay_range=tuple(data["delay_range"]),  # Convert list to tuple
        timeout_seconds=data["timeout_seconds"],
        batch_size=data["batch_size"],
        user_agents=data["user_agents"],
    )
    crawler = Crawler(config)
    results = asyncio.run(crawler.run())
    print(results)
