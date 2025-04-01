#!/bin/bash

# Проверка аргументов
if [ $# -lt 1 ]; then
    echo "Использование: $0 <имя_файла_приложения.py>"
    exit 1
fi

# Имя файла приложения
APP_FILE=$1

# Проверка существования файла
if [ ! -f "$APP_FILE" ]; then
    echo "Ошибка: Файл '$APP_FILE' не найден!"
    exit 1
fi

# Получаем директорию и имя файла
APP_DIR=$(dirname "$APP_FILE")
APP_NAME=$(basename "$APP_FILE")

# Удаление существующего контейнера
docker rm -f pyspark-app 2>/dev/null || true

# Запуск нового контейнера
echo "Запускаем Spark-приложение: $APP_FILE"

docker run -it --name pyspark-app \
    -p 4040:4040 \
    -v "$(pwd)/$APP_FILE:/home/jovyan/work/app.py" \
    jupyter/pyspark-notebook:spark-3.3.2 \
    bash -c "pip install py4j && PYTHONPATH=\$PYTHONPATH:/usr/local/spark/python:/usr/local/spark-3.3.2-bin-hadoop3/python/lib/py4j-0.10.9.5-src.zip python /home/jovyan/work/app.py"

echo "Приложение Spark завершено." 