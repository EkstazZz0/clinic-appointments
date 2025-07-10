Запуск проекта в Docker:

1. git clone https://github.com/EkstazZz0/clinic-appointments
2. cd clinic-appointments
3. cp .env.example .env
4. docker-compose up --build -d

Требуемые ENV переменные:

1. APP_ENV - режим запуска API. Значения только production или test.
2. DB_NAME - название базы данных Postgres для СУБД PostgreSQL и подключения API.
3. DB_USER - имя пользователя Postgres для СУБД PostgreSQL и подключения API.
4. DB_PASSWORD - пароль пользователя PostgreSQL.
5. APP_HOST - IP-адрес, который будет слушать API, принимать запросы и отвечать. 0.0.0.0 - все адреса.
6. HOST_API_PORT - порт на хостируемом Docker-контейнеры сервере, на котором принимает запросы в API и передает в Docker-контейнер API.
7. HOST_DB_PORT -  порт на хостируемом Docker-контейнеры сервере, на котором принимает подключение и работе к PostgreSQL базе данных.
