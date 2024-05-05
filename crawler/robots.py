import urllib.robotparser
from urllib.parse import urlparse


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
