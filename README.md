# CarsApi

## Описание проекта
RESTful API для сбора и фильтрации данных об автомобилях. API поддерживает добавление, обновление, удаление автомобилей, получение списка автомобилей с фильтрами.

## Установка

### 1. Клонирование репозитория
```bash
git clone https://github.com/SobrSergio/CarsApi.git
cd CarsApi
```

### 2. Создание виртуального окружения и установка зависимостей
```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Применение миграций и создание суперпользователя
```bash
python manage.py migrate
python manage.py createsuperuser
```

### 4. Запуск сервера
```bach
python manage.py runserver
```

## Использование API

### Регистрация пользователя
#### Эндпоинт
`POST /api/register/`

#### Пример запроса
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

### Получение токена
#### Эндпоинт
`POST /api/token/`

#### Пример запроса
```json
{
    "username": "your_username",
    "password": "your_password"
}
```

#### Пример ответа
```json
{
    "access": "your_access_token", #использовать для работы с api
    "refresh": "your_refresh_token"
}

```

### Добавление автомобиля
#### Эндпоинт
`POST /api/cars/`

#### Заголовки
```json 
Authorization: Bearer your_access_token
```

#### Пример запроса
```json
{
    "brand": "Audi",
    "model": "A5",
    "year": 2024,
    "fuel_type": "бензин",
    "transmission": "автоматическая",
    "mileage": 5000,
    "price": 100000
}

```

### Получение автомобилей по фильтру 
#### Эндпоинт
`POST /api/cars/brand=Audi&model=A5&year=2024&fuel_type=бензин&transmission=автоматическая&mileage_min=0&mileage_max=10000&price_min=20000&price_max=300000`
`

#### Заголовки
```json 
Authorization: Bearer your_access_token
```

### Получение деталей конкретного автомобиля по ID
#### Эндпоинт
`POST /api/cars/{id}`

#### Заголовки
```json 
Authorization: Bearer your_access_token
```

### Обновление автомобиля
#### Эндпоинт
`PUT /api/cars/{id}`

#### Заголовки
```json 
Authorization: Bearer your_access_token
```

#### Пример запроса
```json
{
    "brand": "Audi",
    "model": "A5",
    "year": 2024,
    "fuel_type": "бензин",
    "transmission": "автоматическая",
    "mileage": 10000,
    "price": 90000
}
```

### Удаление автомобиля
#### Эндпоинт
`DELETE /api/cars/{id}`

#### Заголовки
```json 
Authorization: Bearer your_access_token
```


## Документация API

Документация выполнена благодаря swagger, её можно посмотреть перейдя по ссылкам:

- Swagger UI: [http://127.0.0.1:8000/swagger/](http://127.0.0.1:8000/swagger/)
- Redoc: [http://127.0.0.1:8000/redoc/](http://127.0.0.1:8000/redoc/)
