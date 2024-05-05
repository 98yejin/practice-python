# Crawler

## Objective

## Requirements

-

## How to use?

- batch processing?
  - run by arguments and options
  - need to send alert ( include failed list )
- run by user?
  - GUI or at least pretty and understandable logs

## Checklist

- include multiple urls from same baseurl ?
  - can be blocked by that sites => need some delay
- how many urls?
  - if not much file will be engough
    - good to use version control system
  - but if too many urls, better to use database
- error handling
  - are we gonna handle errors?
    - just logging or retry or stop after ...
    - or nothing
- Respect robots.txt: Always check the robots.txt file of a website to ensure you're allowed to scrape it.
- User-Agent String: Some websites might block requests from scripts, so it's useful to set a user-agent string that mimics a browser.
- Error Handling: Enhance error handling by retrying failed requests or logging errors.
- Scalability: For very large scale scraping tasks, you might need more robust solutions like distributed scraping using frameworks such as Scrapy.
