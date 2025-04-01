#!/usr/bin/env python3

from pyspark.sql import SparkSession
from pyspark.sql.functions import col, lit

print("Запускаем PySpark...")

# Инициализация сессии Spark
spark = SparkSession.builder \
    .appName("SimplePySparkTest") \
    .master("local[*]") \
    .config("spark.ui.port", "4040") \
    .getOrCreate()

# Вывод версии Spark
print("Версия Spark:", spark.version)

# Создание тестового набора данных
data = [
    (1, "Иван", 30),
    (2, "Мария", 25),
    (3, "Петр", 40),
    (4, "Анна", 35),
    (5, "Сергей", 45)
]

# Создание DataFrame
columns = ["id", "name", "age"]
df = spark.createDataFrame(data, columns)

# Вывод схемы и примера данных
print("Схема DataFrame:")
df.printSchema()

print("\nПримеры данных DataFrame:")
df.show()

# Простая трансформация: фильтрация и добавление колонки
result_df = df.filter(col("age") > 30) \
    .withColumn("status", lit("Active"))

print("\nОтфильтрованный DataFrame с новой колонкой:")
result_df.show()

# Простая агрегация
print("\nСредний возраст по статусу:")
result_df.groupBy("status").avg("age").show()

# Информация о Spark сессии
print("\nИнформация о приложении Spark:")
print(f"Имя приложения: {spark.conf.get('spark.app.name')}")
print(f"URL веб-интерфейса: http://localhost:{spark.conf.get('spark.ui.port')}")

print("\nТест PySpark успешно завершен!")

# Ждем небольшое время для проверки UI
import time
print("\nОжидаем 10 секунд для проверки UI...")
time.sleep(10)

# Остановка сессии Spark
spark.stop()
print("Сессия Spark остановлена.") 