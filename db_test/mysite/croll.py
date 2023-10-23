# import requests
# from bs4 import BeautifulSoup

# url = 'https://paullab.co.kr/bookservice/'
# response = requests.get(url)
# response.encoding = 'utf-8'
# html = response.text

# soup = BeautifulSoup(html, 'html.parser')
# data = []

# book_items = soup.select('.book_detail')
# for id, book_item in enumerate(book_items, start=1):
#     title = book_item.select_one('.book_name').text.strip()
#     price = book_item.select('.book_info')[0].text.strip()
#     author = book_item.select('.book_info')[1].text.strip()
#     data.append({"id": id, "title": title, "price": price, "author": author})


# # 데이터베이스에 연결
# conn = sqlite3.connect('homework4.db')

# # 커서 생성
# cursor = conn.cursor()

# # post 테이블 생성
# cursor.execute('CREATE TABLE post (id INTEGER, title TEXT, price INTEGER, author TEXT)')

# # 데이터 삽입
# for item in data:
#     cursor.execute('INSERT INTO post VALUES (?, ?, ?, ?)', (item['id'], item['title'], item['price'], item['author']))

# # 커밋(변경 사항 저장)
# conn.commit()

# cursor.execute('SELECT * FROM post')
# rows = cursor.fetchall()
# column_names = [column[0] for column in cursor.description]
# data = [dict(zip(column_names, row)) for row in rows]
# with open('output.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)
# conn.close()