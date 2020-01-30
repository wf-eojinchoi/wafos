sudo docker run --name pg-docker -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 -v /home/v2washwapos/postgres/pg10:/var/lib/postgresql/data postgres:10
