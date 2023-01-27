# Проект: асинхронный парсер PEP

### Описание
Парсер сайта [PEP](https://peps.python.org/), написанный на асинхронном фреймворке [Scrapy](https://docs.scrapy.org/en/latest/index.html).

Данный парсер позволяет:
 - получить информацию обо всех PEP (номер, название, статус);
 - получить информацию об общем кол-ве статусов.
 
Полученные данные предоставляются в формате ```.csv```

 ### Используемые технологии
  - Python 3.9
  - Scrapy 2.7

### Порядок запуска
1. Клонировать проект.
```
git@github.com:ropek745/scrapy_parser_pep.git
```
2. Создать и активировать виртуальное окружение. Установить зависимости.
```
python -m venv venv #(for Windows)
```
```
python3 -m venv venv #(for MacOs/ Linux)
```
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
3. Запустить парсер
```
scrapy crawl pep
```

## Разработчик - [Роман Пекарев](https://github.com/ropek745) ##

