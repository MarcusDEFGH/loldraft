This repository includes a scrapy spider to build a consistent database about high elo League of Legends games, as well a simple algorithm do provide game predictions based on the team composition alone.

Just run the container:
`docker compose up --build`

Update your database:
`scrapy crawl opgg -o db.json`

The program currently uses a json file as database, there is a woking mongodb pipeline that can be used for that, feel free to send a pull request 😉


Then you just have to enter de `worker` container and run the predict script when everyone have selected their champions.
`docker exec -i -t worker /bin/bash`
