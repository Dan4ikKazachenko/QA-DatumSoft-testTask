import sqlite3

# Создание и подключение к базе данных в памяти
conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

# Создание таблицы Users и вставка данных
cursor.execute('''
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    name TEXT,
    age INTEGER
)
''')
cursor.executemany('''
INSERT INTO Users (name, age) VALUES (?, ?)
''', [
    ('Alice', 25),
    ('Bob', 35),
    ('Charlie', 40)
])

# Выполнение запроса задачи 1
cursor.execute('SELECT name FROM Users WHERE age > 30')
users_over_30 = cursor.fetchall()

# Проверка результата задачи 1 с помощью assert
assert users_over_30 == [('Bob',), ('Charlie',)], f"Expected [('Bob',), ('Charlie',)] but got {users_over_30}"

# Создание таблицы Products и вставка данных
cursor.execute('''
CREATE TABLE Products (
    id INTEGER PRIMARY KEY,
    name TEXT,
    price REAL
)
''')
cursor.executemany('''
INSERT INTO Products (name, price) VALUES (?, ?)
''', [
    ('Product1', 8.5),
    ('Product2', 12.0),
    ('Product3', 9.0)
])

# Выполнение запроса задачи 2
cursor.execute('UPDATE Products SET price = price + (price * 0.10) WHERE price < 10')
conn.commit()

# Проверка результатов обновления
cursor.execute('SELECT name, price FROM Products')
updated_products = cursor.fetchall()

# Ожидаемые результаты после обновления
expected_products = [
    ('Product1', 9.35),  # 8.5 + 10%
    ('Product2', 12.0),  # не изменилось
    ('Product3', 9.9)    # 9.0 + 10%
]

# Проверка результата задачи 2 с помощью assert
assert updated_products == expected_products, f"Expected {expected_products} but got {updated_products}"

# Закрытие соединения
conn.close()

print("Все тесты пройдены успешно")
