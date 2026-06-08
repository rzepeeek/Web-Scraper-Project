from bs4 import BeautifulSoup
import re

def parse_html(html):
    soup = BeautifulSoup(html, "html.parser")

    emails = re.findall(r"[\w\.-]+@[\w\.-]+\.\w+", html)
    phones = re.findall(r"\+?\d[\d\s\-]{8,}\d", html)
    links = [a.get("href") for a in soup.find_all("a") if a.get("href")]

    return {
        "emails": emails,
        "phones": phones,
        "links": links,
        "addresses": []  
    }
