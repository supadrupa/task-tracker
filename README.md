# task-tracker
Task Tracker

## Secret
Initially, you will need to copy file

```bash
cp config/.env.template config/.env
```

## Development start

To start development server inside ``docker`` you will need to run:

```bash
docker-compose build
docker-compose run --rm web python manage.py migrate
docker-compose run --rm web python manage.py createsuperuser
docker-compose up
```

## Api docs link
```
http://127.0.0.1:8000/api/docs/
```