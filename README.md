# Finance Calculator API

Finance Calculator API — небольшое REST-приложение на FastAPI для выполнения простых финансовых расчётов.

Сервис позволяет:

- рассчитывать ежемесячный аннуитетный платёж по кредиту;
- рассчитывать будущую стоимость инвестиции;
- рассчитывать текущую стоимость будущей денежной суммы.

## API endpoints

### Служебные endpoints

- `GET /` — основная информация о сервисе
- `GET /health` — проверка работоспособности приложения
- `GET /version` — версия приложения
- `GET /info` — информация о конфигурации приложения

### Финансовые endpoints

- `GET /loan-payment` — расчёт ежемесячного платежа по кредиту
- `GET /future-value` — расчёт будущей стоимости
- `GET /present-value` — расчёт текущей стоимости

Интерактивная документация FastAPI:

```text
http://127.0.0.1:8000/docs
```

## Требования

Для локального запуска необходимы:

- Python 3.12 или новее;
- pip для установки Python-пакетов.

## Создание виртуального окружения

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## Установка зависимостей

Основные зависимости:

```bash
python -m pip install -r requirements.txt
```

Зависимости для разработки и тестирования:

```bash
python -m pip install -r requirements-dev.txt
```

## Переменные окружения

Приложение использует следующие переменные:

- `APP_NAME` — название приложения
- `APP_AUTHOR` — автор приложения
- `APP_VERSION` — версия приложения
- `APP_CURRENCY` — валюта по умолчанию

Пример:

```bash
export APP_NAME="Finance Calculator API"
export APP_AUTHOR="Gamid"
export APP_VERSION="0.1.0"
export APP_CURRENCY="RUB"
```

Пример конфигурации находится в файле `.env.example`.

Настоящий файл `.env` не должен добавляться в Git.

## Запуск приложения

Для разработки:

```bash
python -m uvicorn app_final:app --reload
```

Для обычного запуска без автоматической перезагрузки:

```bash
python -m uvicorn app_final:app --host 127.0.0.1 --port 8000
```

После запуска приложение доступно по адресу:

```text
http://127.0.0.1:8000
```

Документация:

```text
http://127.0.0.1:8000/docs
```

## Примеры запросов

### Проверка работоспособности

```bash
curl http://127.0.0.1:8000/health
```

Ожидаемый ответ:

```json
{"status":"ok"}
```

### Версия приложения

```bash
curl http://127.0.0.1:8000/version
```

### Информация о приложении

```bash
curl http://127.0.0.1:8000/info
```

### Расчёт платежа по кредиту

```bash
curl "http://127.0.0.1:8000/loan-payment?principal=1000000&annual_rate=12&years=5"
```

### Расчёт будущей стоимости

```bash
curl "http://127.0.0.1:8000/future-value?principal=100000&annual_rate=10&years=3"
```

### Расчёт текущей стоимости

```bash
curl "http://127.0.0.1:8000/present-value?future_value=133100&annual_rate=10&years=3"
```

## Тесты

Для запуска автоматических тестов:

```bash
python -m pytest -v
```

В проекте проверяются:

- `/health`;
- финансовые расчёты;
- работа параметров;
- обработка отсутствующего обязательного параметра.

## Логи

Приложение выводит информацию о выполненных финансовых расчётах в терминал, где запущен Uvicorn.

Пример:

```text
INFO - Calculated future value: principal=100000.0, rate=10.0, years=3, result=133100.0
```

## Диагностика

Проверить используемый Python:

```bash
which python
```

Проверить установку FastAPI и Uvicorn:

```bash
python -m pip show fastapi
python -m pip show uvicorn
```

Проверить работу сервиса:

```bash
curl http://127.0.0.1:8000/health
```

Если порт `8000` занят, можно остановить предыдущий процесс Uvicorn или использовать другой порт.

Например:

```bash
python -m uvicorn app_final:app --host 127.0.0.1 --port 8001
```

## Автор

Gamid