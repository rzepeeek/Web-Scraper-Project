from multiprocessing import Pool
import asyncio
from scraper.async_scraper import scrape_urls
from scraper.parser import parse_html

def process_batch(urls):
    html_pages = asyncio.run(scrape_urls(urls))
    return [parse_html(html) for html in html_pages if html]

def run_parallel(url_batches):
    with Pool() as p:
        results = p.map(process_batch, url_batches)
    return results