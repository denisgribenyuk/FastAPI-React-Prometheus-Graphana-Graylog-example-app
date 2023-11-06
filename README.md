# FastAPI, React, Prometheus, Graphana, Graylog example app


This repository contains code for asynchronous example api using the [Fast Api framework](https://fastapi.tiangolo.com/) ,Uvicorn server, Postgres Database to perform crud operations on items.


## Installation 
1. Ensure [Docker](https://docs.docker.com/install/) is installed.

2. Ensure [Docker Compose](https://docs.docker.com/compose/install/) is installed.
3. create .env file and fill it
   ```
   DATABASE_USER=postgres
   DATABASE_PASSWORD=postgres
   DATABASE_NAME=postgres
   DATABASE_HOST=db
   DATABASE_PORT=5432
   APP_PORT=8000
   GRAFANA_ADMIN_USER=admin
   GRAFANA_ADMIN_PASSWORD=admin
   GRAYLOG_HOST=graylog
   GRAYLOG_PORT_UDP=12201
   GRAYLOG_PASSWORD=somepasswordpepper
   GRAYLOG_PASSWORD_SHA=415e8a6ba1c3eb93e81df34731acc3d60efee685c8e6f7412592a45ba3a0e3b0
   ```

4. Use Docker-Compose to spin up containers

   `docker-compose up -d --build`

5. If everything completes frontend page with notes list should be available on [frontend](http://localhost:8001)

6. Swagger are generated on [Swagger](http://localhost:8000/docs)

## Tests

Tests are available using pytest
Run them using `pytest .` while in the root directory (/Fast-Api-example)

## Documentation

Open API Documentation is provided by [Redoc](http://localhost:8000/redoc)

## Prometheus

Prometheus is provided by [Prometheus](http://localhost:9090)

## Graphana

Graphana is provided by [Graphana](http://localhost:3000)

## Graylog

Graylog is provided by [Graylog](http://localhost:9000). Default admin user is `admin`

## Contributing

Contributions are welcome, please open an issue or submit a PR.

## License

[MIT](https://choosealicense.com/licenses/mit/)
