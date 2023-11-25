import psycopg2


def take_from_bd():
    connection = psycopg2.connect(
            user="myuser",             # ваше имя пользователя в PostgreSQL
            password="ScR26011161",         # ваш пароль
            host="127.0.0.1",                 # адрес сервера базы данных, обычно localhost
            port="5432",                      # порт
            database="II"     # имя вашей базы данных
    )

    # Создание курсора для выполнения SQL-запросов
    cursor = connection.cursor()

    # Выполнение SQL-запроса для выборки данных из колонки 'comment' в таблице 'vk_comments'
    query = "SELECT comment FROM vk_comment"
    cursor.execute(query)

    # Извлечение данных
    comments = cursor.fetchall()

    # Закрытие курсора и соединения
    cursor.close()
    connection.close()

    # Вывод данных

    return comments  # Выводим первое (и единственное) значение из кортежа

# take_from_bd()


def insert_category_theme(category, theme, text_data):
    try:
        connection = psycopg2.connect(
            user="myuser",  # ваше имя пользователя в PostgreSQL
            password="ScR26011161",  # ваш пароль
            host="127.0.0.1",  # адрес сервера базы данных, обычно localhost
            port="5432",  # порт
            database="II"  # имя вашей базы данных
        )

        cursor = connection.cursor()

        # SQL-запрос для вставки категории, темы и текстовых данных в таблицу ai_data_after_vk
        insert_query = "INSERT INTO ai_data_after_vk (category_theme, theme, text_data) VALUES (%s, %s, %s)"

        # Выполняем SQL-запрос
        cursor.execute(insert_query, (category, theme, text_data))

        # Подтверждаем изменения в базе данных
        connection.commit()

        print("Данные успешно вставлены в базу данных")

    except (Exception, psycopg2.Error) as error:
        print("Ошибка при вставке данных в базу данных:", error)

    finally:
        # Закрываем соединение с базой данных
        if connection:
            cursor.close()
            connection.close()