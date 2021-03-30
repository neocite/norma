# norma - our machine learning


# build image for production

```
docker-compose -f docker-compose.prod.yml up -d --build

```

#up

```
docker-compose -f docker-compose.prod.yml exec web python manage.py run
```

# down

```
docker-compose -f docker-compose.prod.yml down -v

```


# reference
https://testdriven.io/blog/dockerizing-flask-with-postgres-gunicorn-and-nginx/

https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-cli-tutorial-fargate.html

https://outline.com/bBfFdF