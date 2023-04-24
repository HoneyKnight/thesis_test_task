# thesis_test_task

## [Задание](https://docs.google.com/document/d/1W_9il7Z3TTp7zJ3KDnwFJnN-FdX9TBXDlslEs12keNc/edit#)

### Запуск в Dev-режиме:
- Установите и активируйте виртуальное окружение
```bash
python -m venv venv
source venv/scripts/activate
```
- Установите зависимости из файла requirements.txt
```bash
pip install -r requirements.txt
```
- Выполните миграции
```bash
python manage.py migrate
```

### Запуск проекта в контейнерах:

В папке infra выполните команду для создания .env файла:

```py
echo '''DB_ENGINE=django.db.backends.postgresql
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
''' > .env
```

#### Сборка контейнеров
```
cd app/infra/
docker-compose up -d --build
docker-compose exec app python manage.py migrate
docker-compose exec app python manage.py collectstatic --no-input
docker-compose exec app python manage.py createsuperuser
```

### Документация:

Документация в dev-режиме:
```
http://127.0.0.1:8000/api/docs/
```

Документация в контейнерах:
```
http://localhost/api/docs/
```