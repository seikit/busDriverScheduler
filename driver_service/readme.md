# Bus service

Microservice focused on managing the bus resource.

## Credentials
The credentials are declared on the .env-* files eg: .env-dev, .env-test, .env-prod. Here are a sample of the .env you should
create to hold the service credentials.

```
CONN=postgresql+psycopg2://db_user:db_pwd@host:port/database
SCHEMA=bus
LOG_LEVEL=INFO
```


