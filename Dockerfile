# pull official base image
FROM python:3.8

# set work directory
WORKDIR /app


# install dependencies
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt


# copy project
COPY . .


# collect static files
# RUN python manage.py collectstatic --noinput
