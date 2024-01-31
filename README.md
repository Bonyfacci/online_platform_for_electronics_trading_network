### Онлайн платформа торговой сети электроники.

### Стек технологий:

 - ![alt text](https://img.shields.io/badge/Python-3.11.5-grey?style=plastic&logo=python&logoColor=white&labelColor=%233776AB)

 - ![alt text](https://img.shields.io/badge/Django-5.0-grey?style=plastic&logo=django&logoColor=white&labelColor=%23092E20)

 - ![alt text](https://img.shields.io/badge/REST_Framework-3.14.0-grey?style=plastic&logo=django&logoColor=white&labelColor=%23092E20)

 - ![alt text](https://img.shields.io/badge/PostgreSQL-15.3-grey?style=plastic&logo=postgresql&logoColor=white&labelColor=%234169E1)



[//]: # ( - ![alt text]&#40;https://img.shields.io/badge/Python-3.11.5-%233776AB?style=plastic&logo=python&logoColor=%233776AB&labelColor=grey&#41;)

[//]: # ( - ![alt text]&#40;https://img.shields.io/badge/Django-5.0-%23092E20?style=plastic&logo=django&logoColor=%23092E20&labelColor=slategrey&#41;)

[//]: # ( - ![alt text]&#40;https://img.shields.io/badge/REST_Framework-3.14.0-%23092E20?style=plastic&logo=django&logoColor=%23092E20&labelColor=slategrey&#41;)

[//]: # ( - ![alt text]&#40;https://img.shields.io/badge/PostgreSQL-15.3-%234169E1?style=plastic&logo=postgresql&logoColor=deepskyblue&labelColor=grey&#41;)

### Описание проекта
Реализована модель сети по продаже электроники.  
Сеть представляет собой иерархическую структуру из 3 уровней:  
 - Завод;  
 - Розничная сеть;  
 - Индивидуальный предприниматель.

Каждое звено сети ссылается только на одного поставщика оборудования.  
Сделан вывод в админ-панели созданных объектов.  
На странице объекта сети добавлено:
 - ссылка на «Поставщика»;
 - фильтр по названию города;
 - «admin action», очищающий задолженность перед поставщиком у выбранных объектов.

Создан набор представлений с помощью DRF.  
Создан запрет на обновление через API поля «Задолженность перед поставщиком»
Настроены права доступа к API.

### Для запуска через консоль необходимо:

 - Клонировать проект на собственный диск в новом каталоге
 - Создать виртуальное окружение
 - Установить зависимости командой:
```python
    pip install -r requirements.txt
```
 - Прописать переменные окружения в файле `.env.sample`
```dotenv
SECRET_KEY='Секретный ключ Django'
DEBUG='True/False', например: True

POSTGRES_DB_NAME='Название базы данных', например: 'name_of_db' или 'my_project'
POSTGRES_DB_USER='Пользователь базы данных', например: 'db_user' или 'postgres'
POSTGRES_DB_PASSWORD='Пароль пользователя базы данных', например: 'your_password'
POSTGRES_DB_HOST='Хост базы данных', например: '127.0.0.1' или 'localhost' или 'db' (для Docker)
POSTGRES_DB_PORT='Порт базы данных', например: '5432'
```
 - Создать базу данных (в данной работе используется PostgreSQL)
```python
    psql -U postgres
    create database trading_network;
    \q
```
 - В терминале выполнить команды:
```python
    python manage.py migrate
```
```python
    python manage.py runserver
```

 - Для создания тестовых пользователей - администратор, менеджер, пользователь:
```python
    python manage.py csu
```
```python
    python manage.py cm
```
```python
    python manage.py cu
```

### Для запуска через Docker необходимо:

 - происходит сборка образа контейнера согласно инструкции в файле Dockerfile
```python
    docker-compose build
```
 - происходит последовательный запуск всех контейнеров согласно инструкции в файле docker-compose.yaml
```python
    docker-compose up
```

### Для завершения работы необходимо:

 - Нажать комбинацию клавиш `CTRL + C` в окне терминала
