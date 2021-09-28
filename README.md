# Recipe API

## Getting started

1. Run

```shell
docker build .
```

```shell
docker-compose build
```

2. Run tests

```shell
docker-compose run app sh -c "python manage.py test"
```

3. Run tests with linting

```shell
docker-compose run app sh -c "python manage.py test && flake8"
```
