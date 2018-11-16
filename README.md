# Поиск дубликатов файлов

Скрипт ищет в указанной директории дуюликаты файлов (сравнивается имя файла и размер в байтах), включая все подпапки.

#Запуск скрипта

При запуске скрипту в качестве аргумента необходимо передать путь к директории.
Понадобится установленный интерпретатор Python, версии 3.5
Пример запуска на Linux:

```bash
$ python3 duplicates.py /home/yulia/devman/duplo/
alco_shops.json, file size is 898324 bytes:
/home/yulia/devman/duplo/alco_shops.json
/home/yulia/devman/duplo/first folder/alco_shops.json
/home/yulia/devman/duplo/second folder/alco_shops.json

```

# Project Goals

The code is written for educational purposes. Training course for web-developers - [DEVMAN.org](https://devman.org)
