# Code-highlighting

 + Сделал выдачу постов и разбивку этих постов на категории благодаря языку шаблонов Django.
 + Реализовал поиск по названиям в постах благодаря запросам к БД через Django.
 + Реализовал просмотры с помощью F выражений и обновлению объектов БД.
 + Сделал топ постов (по просмотрам) и вывод всех тегов, которые есть на сайте с помощью шаблонных тегов и Django ORM.
 + Реализовал пагинацию с помощью классов и языку шаблонов Django.


## Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/lolevan/Code-highlighting.git
```

```
cd Code-highlighting
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source venv/Scripts/activate
```

или

```
source venv/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --no-cache-dir -r requirements.txt
```

Сделать и выполнить миграции:

```
python manage.py makemigrations && python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

Перейти по ссылке:

```
http://127.0.0.1:8000/
```
