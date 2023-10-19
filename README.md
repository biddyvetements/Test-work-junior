Конечная инструкция по запуску Docker контейнеров и отправке POST-запроса к серверу выглядит следующим образом:
Инструкция по запуску Docker контейнера PostgreSQL:
Загрузите Docker образ PostgreSQL, выполнив следующую команду:
    
    $ docker pull postgres
    



Запустите Docker контейнер PostgreSQL с заданными параметрами, выполнив следующую команду:


    $ docker run -itd -e POSTGRES_USER=baeldung -e POSTGRES_PASSWORD=baeldung -p 5432:5432 -v /data:/var/lib/postgresql/data --name postgresql postgres

Инструкция по запуску Docker контейнера с приложением:
Загрузите Docker образ с вашим приложением, заменив "b3nz0/python-docker:tag" на фактический тег образа, выполнив следующую команду:

    
 
    $ docker pull b3nz0/python-docker:tag

Запустите Docker контейнер с вашим приложением, заменив "b3nz0/python-docker:tag" на фактический тег образа, выполнив следующую команду:


    $ docker run -p 5000:5000 b3nz0/python-docker:tag
