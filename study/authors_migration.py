import sqlite3


conn = sqlite3.connect('db.sqlite3')
print('Connected to database successfully.')

c = conn.cursor()

c.execute('select id, author_id, author_2nd_id, author_3rd_id from bookshelf_book where author_id is not null ORDER BY id')
# print(c.fetchall())
# for book in c.fetchall():
#     msg = "ID: %d, Author: %d" % (book[0], book[1])
#     if book[2]:
#         msg += ', 2nd Author: %d' % book[2]
#     if book[3]:
#         msg += ', 3rd Author: %d' % book[3]
#
#     print(msg)

for book in c.fetchall():
    c.execute('INSERT INTO bookshelf_book_authors (book_id, author_id) VALUES (?, ?)', (book[0], book[1],))
    if book[2]:
        c.execute('INSERT INTO bookshelf_book_authors (book_id, author_id) VALUES (?, ?)', (book[0], book[2],))
    if book[3]:
        c.execute('INSERT INTO bookshelf_book_authors (book_id, author_id) VALUES (?, ?)', (book[0], book[3],))

conn.commit()
conn.close()