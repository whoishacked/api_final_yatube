# Yatube.API
## Описание
Проект  Yatube.API. Что можно делать при помощи этого API:
* создавать статьи;
* добавлять статьи в группы;
* оставлять комментарии
* полписываться на понравившихся авторов.
## Установка
Клонируем репозиторий:\
```git clone whoishacked/api_final_yatube```\
Переходим в папку с проектом:\
```cd api_final_yatube```\
Устанавливаем и активируем venv:\
```python3 -m venv venv```\
```source venv/bin/activate```\
Устанавливаем pip:\
```python3 -m pip install --upgrade pip```\
Устанавливаем зависимости:\
```pip instal -r requirements.txt```\
Запускаем проект:\
```python3 manage.py runserver```
----
По адресу `http://127.0.0.1:8000/redoc/` будет доступен список ендпоинтов.