import aiohttp
import asyncio
from typing import List, Optional
from bs4 import BeautifulSoup
from dataclasses import dataclass


@dataclass
class CrawlResult:
    url: str
    content: Optional[str] = None
    error: Optional[str] = None


async def fetch_url(session: aiohttp.ClientSession, url: str) -> CrawlResult:
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            html = await response.text()
            soup = BeautifulSoup(html, "html.parser")
            text = soup.getText(separator="\n", strip=True)
            return CrawlResult(url=url, content=text)
    except Exception as e:
        print(f"[ERROR] {type(e).__name__}: {e}")
        return CrawlResult(url=url, error=str(e))


async def process_batch(urls: List[str], timeout_seconds=3) -> List[CrawlResult]:
    timeout = aiohttp.ClientTimeout(total=timeout_seconds)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        results = await asyncio.gather(
            *[fetch_url(session=session, url=url) for url in urls]
        )
        return results


async def main(urls: List[str], batch_size=10):
    batches = [urls[i : i + batch_size] for i in range(0, len(urls), batch_size)]
    return await asyncio.gather(*[process_batch(batch) for batch in batches])


if __name__ == "__main__":
    urls = [
        "http://example.com/page1",
        "http://example.com/page2",
        "http://example.com/page3",
        # "https://98yejin.github.io",
    ]
    results = asyncio.run(main(urls))
    print(results)
