# Телефонный ассистент

## Задание
Для задачи на computer science кроме решения, напиши тесты с использованием pytest, покрой им основные юзкейсы

Дано список номеров телефонов. Написать программу, которая при вводе первых цифр номера телефона будет возвращать до 10 вариантов номеров телеофонов из базы данных, которые начинаются с введенных цифр.

Пример.
Список номеров телефонов:
380675674432
380672832500
380983567721

In: 380
Out: [380675674432, 380672832500, 380983567721]

In: 38067
Out: [380675674432, 380672832500]

In: 380983
Out: [380983567721]

## Using
Репозиторий: https://github.com/vodono/filex
Деплой проекта: https://fileex.herokuapp.com/

#### Для запуска проекта локально нужно:
1) создать виртуальное окружение Python и активировать его:
    ```linux
    $ virtualenv venv --python=/usr/local/bin/python3.7
    $ . venv/bin/activate
    ```
1) установить необходимые пакеты:
    ```linux
    $ pip install -r requirements.txt
    ``` 
1) создать базу Postgres в консоли саймой БД:
    ```sql
     # create role filex with createdb createrole login encrypted password 'files';
     # create database files with owner=filex encoding=UTF8;
    ```
1) применить миграции к созданной БД в терминале ОС в папке проекта file_ex:
    ```linux
    $ python src/manage.py upgrade
    ```
1) запустить веб-серверв терминале ОС в папке проекта file_ex:
    ```linux
    $ python src/local_run.py
    ```
1) локальный веб-сайт будет доступен по адресу http://127.0.0.1:5000/

#### Для запуска проекта на сайте heroku.com:
1) создать аккаунт на heroku.com установить консоль:
    ```linux
    $ sudo snap install --classic heroku
    ```
1) создать проект (название может быть не доступно):
    ```linux
    $ heroku apps:create fileex
    ```
1) через команды git сохранить проект на remote (heroku or other, данный проект подключен к своему аккаунту github):
    ```linux
    $ git push heroku master
    ```
1) добавляем postgres:
    ```linux
    $ heroku addons:create heroku-postgresql:hobby-dev --app fileex
    ```
1) применить миграции:
    ```linux
    $ heroku run python src/manage.py db upgrade --app fileex
    ```
1) сайт доступен по адресу: https://fileex.herokuapp.com/
а