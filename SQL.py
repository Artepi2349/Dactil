import sqlite3
id = ''
print('Выберите режим: select - S, update - U')
mode = input()
print('Введите слово:')
word = input()
length = len(word)
connection = sqlite3.connect('words.db')
cursor = connection.cursor()

def select(a,b):
    cursor.execute(f'INSERT INTO Words (word, length) VALUES (?, ?)', (a, b))

def update(a,b):
    cursor.execute('UPDATE Words SET word = ? WHERE id = ?', (a, b))


if mode == 'S':
    select(word,length)
elif mode == 'U':
    print('Введите id слова, которое надо изменить:')
    id = input()
    update(word,id)
else:
    print('Выбран неверный режим работы, попробуйте снова')

connection.commit()
connection.close()