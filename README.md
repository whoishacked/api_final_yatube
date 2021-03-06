# Yatube.API
## Описание
Проект **Yatube.API** сделан в рамках обучения программированию на 
языке Python в Yandex Practicum. В спринте рассматривались возможности **Django 
REST Framework**.

Что можно делать при помощи этого API:
* создавать статьи;
* добавлять статьи в группы;
* оставлять комментарии
* полписываться на понравившихся авторов.
## Установка
Клонируем репозиторий:
```
git clone whoishacked/api_final_yatube
```
Переходим в папку с проектом:
```
cd api_final_yatube
```
Устанавливаем и активируем venv:
```
python3 -m venv venv
```
```
source venv/bin/activate
```
Устанавливаем pip:
```
python3 -m pip install --upgrade pip
```
Устанавливаем зависимости:
```
pip instal -r requirements.txt
```
Запускаем проект:
```
python3 manage.py runserver
```
## Примеры
Получить список всех публикаций. При указании параметров limit и offset выдача 
работает с пагинацией:
```
GET /api/v1/posts/
``` 
Получение всех комментариев к публикации:
```
GET /api/v1/posts/{post_id}/comments/
```
Получение списка доступных сообществ:
```
GET /api/v1/groups/
```
Возвращает все подписки пользователя, сделавшего запрос:
```
GET /api/v1/follow/
```
Более подробная информация о возможностях API доступна на странице:
```
http://127.0.0.1:8000/redoc/
```
## Используемые технологии
Краткий список:
- Django 2.2.16
- PyJWT 2.1.0
- djoser 2.1.0
- djangorestframework 3.12.4

Полный список доступен в **requirements.txt**

## Об авторе
**Кутузов Андрей:**
- Telegram: @andrewkutuzov
- Email: britvill@gmail.com
