FROM python:3.11

WORKDIR /app
COPY . .
RUN pip install flask aiohttp beautifulsoup4 pymongo

CMD ["python", "main.py"]