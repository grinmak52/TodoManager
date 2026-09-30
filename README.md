# TodoManager

Простое приложение для управления задачами (To-Do) с категориями. Backend на FastAPI, frontend на React.

## Стек

**Backend**
- FastAPI
- SQLAlchemy 2.x (async) + asyncpg
- Alembic — миграции БД
- Pydantic v2 / pydantic-settings
- PostgreSQL
- Poetry — управление зависимостями

**Frontend**
- React (Create React App)

## Структура проекта

```
TodoManager/
├── todo-app-backend/
│   ├── src/
│   │   ├── main.py              # точка входа, создание FastAPI-приложения
│   │   ├── core/
│   │   │   └── config.py        # настройки приложения (.env)
│   │   ├── orm/
│   │   │   ├── base.py          # Base, naming convention
│   │   │   ├── db_helper.py     # engine, session factory
│   │   │   ├── mixins/          # переиспользуемые миксины моделей
│   │   │   └── models/          # ORM-модели (Task, Category)
│   │   ├── schemas/              # Pydantic-схемы (Create/Read/Update)
│   │   ├── repositories/         # слой доступа к БД
│   │   ├── services/              # бизнес-логика
│   │   ├── api/
│   │   │   ├── dependencies.py   # Depends для сервисов/сессии
│   │   │   └── api_v1/           # роутеры эндпоинтов
│   │   ├── alembic/               # миграции БД
│   │   └── utils/
│   ├── pyproject.toml
│   └── poetry.lock
└── todo-app-frontend/
    ├── src/
    └── public/
```

## Backend: установка и запуск

### 1. Установить зависимости

```bash
cd todo-app-backend
poetry install
```

### 2. Настроить переменные окружения

Скопируйте шаблон и заполните своими значениями:

```bash
cd src
cp .env.template .env
```

Минимально нужно указать строку подключения к PostgreSQL:

```
APP_CONFIG__DB__URL=postgresql+asyncpg://user:password@localhost:5432/database
APP_CONFIG__DB__ECHO=0
```

### 3. Поднять базу данных

Нужен запущенный PostgreSQL (локально или в Docker), соответствующий данным из `.env`.

### 4. Применить миграции

```bash
poetry run alembic revision --autogenerate -m "create tasks and categories tables"
poetry run alembic upgrade head
```

### 5. Запустить сервер

```bash
poetry run python main.py
```

По умолчанию сервер поднимется на `http://127.0.0.1:8080` (адрес и порт настраиваются в `.env` через `APP_CONFIG__RUN__HOST` / `APP_CONFIG__RUN__PORT`).

Документация API (Swagger) доступна на `http://127.0.0.1:8080/docs`.

## Frontend: установка и запуск

```bash
cd todo-app-frontend
npm install
npm start
```

По умолчанию React-приложение поднимется на `http://localhost:3000`.

> Убедитесь, что адрес фронтенда указан в `APP_CONFIG__CORS__CORS_ORIGINS` в `.env` бэкенда, иначе запросы будут блокироваться политикой CORS.

## API

| Метод | Путь | Описание |
|---|---|---|
| GET | `/tasks` | Список задач |
| POST | `/tasks` | Создать задачу |
| PATCH | `/tasks/{task_id}` | Обновить задачу |
| DELETE | `/tasks/{task_id}` | Удалить задачу |
| GET | `/categories` | Список категорий |
| POST | `/categories` | Создать категорию |
| PATCH | `/categories/{category_id}` | Обновить категорию |
| DELETE | `/categories/{category_id}` | Удалить категорию |

## Работа с миграциями

Создать новую миграцию после изменения моделей:
```bash
poetry run alembic revision --autogenerate -m "описание изменений"
```

Применить миграции:
```bash
poetry run alembic upgrade head
```

Откатить последнюю миграцию:
```bash
poetry run alembic downgrade -1
```

> Не забывайте импортировать каждую новую модель в `orm/models/__init__.py` — иначе Alembic не увидит изменений и автогенерация создаст пустую миграцию.
