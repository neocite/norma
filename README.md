# norma - our machine learning


# build image for production

```
docker-compose -f docker-compose.prod.yml up -d --build

```

# down

```
docker-compose -f docker-compose.prod.yml down -v

```

# reference
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/