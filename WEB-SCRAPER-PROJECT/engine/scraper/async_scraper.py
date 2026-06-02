import aiohttp
import asyncio

# funkcja asynchroniczna pobierajaca zawartosc strony
async def fetch(session, url):
    try:
        # wysylanie zapytania HTTP GET do podanego URL
        async with session.get(url, timeout=10) as response:
            # zwrocenie tekstu strony (HTML)
            return await response.text()
    except:
        # w przypadku bledu (np. brak polaczenia) zwracany jest pusty string
        return ""

# funkcja asynchroniczna pobierajaca wiele stron jednoczesnie
async def scrape_urls(urls):
    async with aiohttp.ClientSession() as session:
        tasks = [fetch(session, url) for url in urls]
        return await asyncio.gather(*tasks)