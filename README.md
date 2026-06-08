# 🌍 Web Scraper Project (Distributed System)

System do pobierania i analizy danych ze stron internetowych, działający w architekturze rozproszonej.

---

## 📖 Opis projektu

Aplikacja umożliwia użytkownikowi wprowadzenie jednego lub wielu adresów URL poprzez interfejs webowy.

Podane strony są następnie asynchronicznie pobierane i analizowane przez silnik scrapujący. Z wykorzystaniem biblioteki BeautifulSoup wyodrębniane są różne grupy danych, które następnie zapisywane są w bazie MongoDB.

### 📌 Profil pobieranych danych

* 📄 Tytuł strony (HTML Title)
* 📧 Adresy e-mail
* 📞 Numery telefonów
* 🔗 Linki (href)
* 📰 Nagłówki H1
* 📑 Nagłówki H2
* 🏷️ Meta Description

---

## 🧩 Architektura systemu

Projekt został podzielony na trzy niezależne moduły:

* 🖥 **Interface (Flask + HTML/CSS)** – formularz do wprowadzania adresów URL
* ⚙️ **Engine (asyncio + multiprocessing + BeautifulSoup)** – równoległe pobieranie i analiza danych
* 🗄 **MongoDB** – przechowywanie wyników scrapowania

📦 Wszystkie moduły działają w osobnych kontenerach Docker zarządzanych przez Docker Compose.

```text
[ INTERFACE ] → [ ENGINE ] → [ MONGO DB ]
```

---

## 🛠 Technologie

* Python 3
* Flask
* aiohttp
* asyncio
* multiprocessing
* BeautifulSoup4
* HTML / CSS
* MongoDB
* Docker
* Docker Compose

---

## ▶️ Uruchomienie

```bash
git clone https://github.com/rzepeeek/Web-Scraper-Project.git
cd WEB-SCRAPER-PROJECT
docker-compose up --build
```

🌐 Aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:5000
```

---

## 📝 Instrukcja użycia

1. Wprowadź jeden lub więcej adresów URL.
2. Kliknij **Start Scrapowania**.
3. Aplikacja rozpocznie pobieranie i analizę danych.
4. Wyniki zostaną zapisane w bazie MongoDB.

Przykładowe strony testowe:

```text
https://www.wp.pl
https://www.mongodb.com/contact
https://www.mongodb.com/products/subscription/order-confirmation
```

---

## 🗃️ Sprawdzenie wyników

Dane można sprawdzić za pomocą MongoDB Compass lub z poziomu terminala.

Uruchomienie konsoli MongoDB:

```bash
docker exec -it web-scraper-project-mongo-1 mongosh
```

Następnie:

```javascript
use scraper_db
db.data.find().pretty()
```

Liczbę zapisanych stron można sprawdzić poleceniem:

```javascript
db.data.countDocuments()
```

---

## 🔍 Testowanie

* Testy przeprowadzono lokalnie (Windows + Docker Desktop)
* Zweryfikowano poprawność komunikacji pomiędzy modułami
* Sprawdzono poprawność zapisu danych do MongoDB
* Potwierdzono równoległe przetwarzanie wielu adresów URL
* Zweryfikowano poprawne wyodrębnianie tytułów stron, nagłówków HTML oraz metadanych

---

## 🚧 Dalszy rozwój

* 📊 Wyświetlanie wyników bezpośrednio w interfejsie webowym
* 🏠 Wykrywanie adresów pocztowych i obrazów
* 📬 Rozbudowa parsera o dodatkowe typy danych
* 🎨 Rozbudowa interfejsu użytkownika
* ☁️ Skalowanie aplikacji na wiele instancji

---

## 👨‍💻 Autorzy

* Adrian Czarnota 21442
* Dawid Rzepka 21299

**ANS w Elblągu**
**Przetwarzanie równoległe i rozproszone**
