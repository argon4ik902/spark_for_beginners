# PySpark в Docker

Этот проект предоставляет простую настройку для запуска приложений Apache Spark с использованием PySpark в контейнере Docker.

## Требования

- Docker
- Docker Compose (опционально)

## Установка и запуск

### Способ 1: Использование Docker Compose

1. Клонируйте репозиторий:
   ```bash
   git clone <url-репозитория>
   cd spark
   ```

2. Запустите контейнер с Jupyter Notebook:
   ```bash
   docker-compose up
   ```

3. Откройте Jupyter Notebook в браузере:
   ```
   http://localhost:8888
   ```

4. Приложения Spark UI доступны по адресу:
   ```
   http://localhost:4040
   ```

### Способ 2: Запуск отдельных приложений

Для запуска отдельных Python-скриптов в контейнере можно использовать скрипт `run_spark_app.sh`:

1. Сделайте скрипт исполняемым:
   ```bash
   chmod +x run_spark_app.sh
   ```

2. Запустите ваше приложение:
   ```bash
   ./run_spark_app.sh apps/example_app.py
   ```

## Структура проекта

- `apps/` - директория для Spark-приложений
  - `example_app.py` - пример простого приложения PySpark
- `docker-compose.yml` - конфигурация Docker Compose
- `run_spark_app.sh` - скрипт для запуска отдельных приложений

## Пример PySpark-приложения

В директории `apps/` есть пример приложения `example_app.py`, которое демонстрирует основные возможности PySpark:
- Создание SparkSession
- Работа с DataFrame
- Фильтрация и трансформация данных
- Агрегация
- Доступ к Spark UI

## Запуск своих приложений

1. Создайте Python-скрипт в директории `apps/`
2. Импортируйте необходимые библиотеки PySpark:
   ```python
   from pyspark.sql import SparkSession
   from pyspark.sql.functions import col, lit
   ```

3. Создайте SparkSession:
   ```python
   spark = SparkSession.builder \
       .appName("MySparkApp") \
       .master("local[*]") \
       .config("spark.ui.port", "4040") \
       .getOrCreate()
   ```

4. Запустите скрипт с помощью `run_spark_app.sh`:
   ```bash
   ./run_spark_app.sh apps/my_app.py
   ```

## Полезные команды

- Остановка контейнера:
  ```bash
  docker-compose down
  ```

- Проверка логов:
  ```bash
  docker-compose logs
  ```

- Подключение к работающему контейнеру:
  ```bash
  docker exec -it pyspark-app bash
  ``` 