# Форма авторизации для пробного демоэкза

Стек: python(tkinter), PostgreSQL (через алхимию)

# Как запустить:

1. Установите зависимости:
   `pip install -r requirements.txt`

2. В PostgreSQL создайте базу данных `form_db`:
    `createdb form_db`

3. Выполните SQL-скрипт из файла `database.sql` (он создаст таблицу `users` и добавит тестовых пользователей):
    `psql -d form_db -f database.sql`

4. В корне проекта создайте файл `.env` и вставьте туда одну из этих строк:

   **Если у вас винда или при установке задали пароль:**
   `DATABASE_URL=postgresql+psycopg2://postgres:ВАШ_ПАРОЛЬ@localhost:5432/form_db`
   (Вместо ВАШ_ПАРОЛЬ напишите ваш пароль от PostgreSQL, например: postgres:12345)

   **Если у вас Mac и база установлена через Homebrew:**
   `DATABASE_URL=postgresql+psycopg2://localhost:5432/form_db`
5. Запустите программу:
   `python main.py`

## Тестовые аккаунты:
- admin1 / admin123
- manager_chelsea / manager123
- just_user / user123