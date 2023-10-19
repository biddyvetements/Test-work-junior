Конечная инструкция по запуску Docker контейнеров и отправке POST-запроса к серверу выглядит следующим образом:
Инструкция по запуску Docker контейнера PostgreSQL:
Загрузите Docker образ PostgreSQL, выполнив следующую команду:
    
    $ docker pull postgres
    



Запустите Docker контейнер PostgreSQL с заданными параметрами, выполнив следующую команду:


    $ docker run -itd -e POSTGRES_USER=baeldung -e POSTGRES_PASSWORD=baeldung -p 5432:5432 -v /data:/var/lib/postgresql/data --name postgresql postgres

Инструкция по запуску Docker контейнера с приложением:
Загрузите Docker образ с вашим приложением, заменив "b3nz0/python-docker:tag" на фактический тег образа, выполнив следующую команду:

    
 
    $ docker pull b3nz0/python-docker:latest

Запустите Docker контейнер с вашим приложением, заменив "b3nz0/python-docker:tag" на фактический тег образа, выполнив следующую команду:


    $ docker run -p 3000:3000 b3nz0/python-docker:latest

**Отправка POST-запроса к серверу:**

Пример запроса:

`POST /api/questions/ HTTP/1.1
Host: 212.193.51.197:3000
Content-Type: application/json
Content-Length: 20
{"questions_num":10}`

Пример ответа:

`{
    "success": true,
    "latest_question": {
        "id": 143953,
        "answer": "(Joyce) Kilmer",
        "question": "This \"Trees\" poet was posthumously awarded the Croix de Guerre",
        "value": 600,
        "airdate": "2010-12-22T20:00:00.000Z",
        "created_at": "2022-12-30T20:26:58.406Z",
        "updated_at": "2022-12-30T20:26:58.406Z",
        "category_id": 16810,
        "game_id": 3534,
        "invalid_count": null,
        "category": {
            "id": 16810,
            "title": "joyce to the world",
            "created_at": "2022-12-30T20:26:57.580Z",
            "updated_at": "2022-12-30T20:26:57.580Z",
            "clues_count": 5
        }
    }
} `