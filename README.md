# django Github Base Setup

# Setup
## Run locally
```
$ python manage.py runserver
```

## Run locally in docker with docker compose
If you want to rebuild:
```
$ docker-compose up --build
```
Otherwise:
```
$ docker-compose up
```


### Running migrations
```
$ docker-compose run web /usr/local/bin/python manage.py migrate
```
### Create superuser
```
$ docker-compose run web /usr/local/bin/python manage.py createsuperuser
```
### Collect static
```
$ docker-compose run web /usr/local/bin/python manage.py collectstatic  --noinput
```


# Update all packages in venv
```
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
```


# Sources
* https://testdriven.io/blog/deploying-django-to-heroku-with-docker/
* https://hacksoft.io/github-actions-in-action-setting-up-django-and-postgres/ (github actions)