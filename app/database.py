import psycopg2
from config import HOST, USER, PASSWORD, DB_NAME

# Создание таблицы
def create_table_nomenclature(cursor):
    cursor.execute(
        """CREATE TABLE nomenclature(
            id serial PRIMARY KEY,
            name CHARACTER VARYING(30) NOT NULL,
            price REAL NOT NULL,
            amount INTEGER);"""
    )
    print("[INFO] Таблица создана")

def create_table_client(cursor):
    cursor.execute(
        """CREATE TABLE nomenclature(
            id serial PRIMARY KEY,
            name CHARACTER VARYING(30) NOT NULL,
            address CHARACTER VARYING(30) NOT NULL;"""
    )
    print("[INFO] Таблица создана")



def main():
    try:
        # Подключение к базе данных
        connection = psycopg2.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            database=DB_NAME
        )
        connection.autocommit = True

        # Создание таблицы
        with connection.cursor() as cursor:
            create_table_nomenclature(cursor)
            create_table_client(cursor)


    except Exception as _ex:
        print("[INFO] Ошибка при работе с PostgreSQL", _ex)
    finally:
        if connection:
            connection.close()
            print("[INFO] PostgreSQL соединение закрыто")


if __name__ == "__main__":
    main()