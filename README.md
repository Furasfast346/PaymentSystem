# Payment System — Django + Stripe

Реализован полноценный Django-сервер с интеграцией Stripe Checkout для оплаты товаров и заказов.

## Что реализовано

**Основное задание:**
- Модель `Item` (name, description, price)
- GET `/item/{id}` — красивая HTML-страница товара с кнопкой «Купить»
- GET `/buy-item/{id}` — создание Stripe Checkout Session
- JS + Stripe.js для редиректа на Checkout форму

**Бонусные задачи (выполнены):**
- Модель `Order` + `OrderItem` (корзина с несколькими товарами)
- Модели `Discount` и `Tax` 
- Полноценная Django Admin-панель
- Запуск через Docker + `docker-compose.yml`
- Использование `.env` и переменных окружения
- Деплой на сервер

**Не реализовано:**
- Stripe Payment Intent вместо Session
- Две разные валюты с отдельными Keypair

## Технологии

- **Backend**: Django 6.0.4, Python 3.13
- **Платежи**: Stripe Checkout Sessions
- **База данных**: SQLite (`db.sqlite3` лежит в репозитории для удобства демо)
- **Сервер**: Gunicorn (в Docker)
- **Контейнеризация**: Docker + docker-compose
- **Frontend**: Bootstrap 5 + vanilla JavaScript


## Креды от админки

Логин: furasfast
Пароль: 0000
В админке удобно добавлять товары, заказы, скидки и налоги.

## Ссылка на сайт

https://paymentsystem-xlvo.onrender.com/

## 🚀 Быстрый запуск

### 1. Локально (без Docker)

```bash
cd PaymentSystem
python -m venv venv
source venv/bin/activate          # Windows: venv\Scripts\activate
pip install -r requirements.txt

cp .env.example .env
# Открой PaymentSystem/.env и вставь свои тестовые ключи Stripe

python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
Открывай: http://127.0.0.1:8000

### 2. Через Docker (рекомендуется)
```bash
# Скопировать переменные окружения в файл .env
cp PaymentSystem/.env.example PaymentSystem/.env

# Запустить контейнер
docker compose up
```
Открывай: http://localhost:8000

Остановить контейнеры:
```bash
docker compose down
```

