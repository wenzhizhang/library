import sqlite3

isbn_list = [
'9787208166714',
]

conn = sqlite3.connect('db.sqlite3')
c = conn.cursor()
print('Open database successfully.')
for isbn in isbn_list:
    image_url = 'image/books/{}.png'.format(isbn)
    print(image_url)
    c.execute("UPDATE bookshelf_book SET thumb_image = '{}' where isbn='{}'".format(image_url, isbn))
conn.commit()
print("Total number of rows updated :", conn.total_changes)