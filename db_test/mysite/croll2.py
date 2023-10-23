# - 코드를 한 블록으로 만들어서 스터디 방에 업로드 해주세요.
#     요구사항1. book 크롤링한 데이터를 데이터베이스에 담아야 합니다.
#         - 데이터베이스를 생성
#         - 크롤링
#         - id, title, price, author
#     요구사항2. 데이터베이스를 읽습니다.
#     요구사항3. 데이터베이스를 JSON 형태로 출력해야 합니다. 출력 이름은 output.json

import requests
from bs4 import BeautifulSoup
import sqlite3
import json

class Book:

    def __init__(self, title, price, authors):
        self.title = title
        self.price = price
        self.authors = authors
        self.author = [author.strip() for author in authors.split(",")]

    def __str__(self):
        return f"Book({self.title}, {self.price}, {self.author})"

    def __repr__(self):
        return f"Book({self.title}, {self.price}, {self.author})"

    def to_dict(self):
        return {
            "title": self.title,
            "price": self.price,
            "author": self.author,
        }

    def to_list(self):
        return [self.title, self.price, self.author]

# 요구사항 1. book 크롤링한 데이터를 데이터베이스에 담기
url = 'https://paullab.co.kr/bookservice/'
response = requests.get(url)
response.encoding = 'utf-8'
html = response.text

soup = BeautifulSoup(html, 'html.parser')
book_details = soup.select('.book_detail')

books_data = []
for item in book_details:
    book_name = item.select('.book_name')[0].text.strip()
    book_price = int(item.select('.book_info')[0].text[3:].strip().replace(',', '').replace('무료', '0').replace('원', ''))
    book_author = item.select('.book_info')[1].text[3:].strip()
    books_data.append(Book(book_name, book_price, book_author))

print(books_data)

db = sqlite3.connect('books.db')
conn = db.cursor()

## 데이터베이스를 생성
conn.execute("CREATE TABLE book_crawler (id INTEGER, title TEXT, price INTEGER, author TEXT)")

## 데이터 삽입
for idx, item in enumerate(books_data, 1):
    conn.execute(f"INSERT INTO book_crawler VALUES ({idx}, '{item.title}', '{item.price}', '{item.authors}')")

db.commit()
db.close()

# 요구사항2. 데이터베이스를 읽습니다.
db = sqlite3.connect('books.db')
conn = db.cursor()

## 데이터 rows에 가져오기
rows = conn.execute("SELECT id, title, price, author FROM book_crawler")


# 요구사항3. 데이터베이스를 JSON 형태로 출력하기. 출력 이름은 output.json
rows_array = []
for row in rows:
    rows_array.append({
        'id': row[0],
        'title': row[1],
        'price': row[2],
        'author': row[3]
    })

with open('output.json', 'w', encoding='utf-8') as f:
    json.dump(rows_array, f, ensure_ascii=False, indent=4)

db.close()