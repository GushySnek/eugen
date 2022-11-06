FROM python:3.10

WORKDIR /app
# RUN pip install numpy discord
COPY ./eugen .
# COPY pyproject.toml poetry.lock .
# RUN poetry export -f requirements.txt --output requirements.txt
# RUN pip install -r /eugen/requirements.txt
CMD ["python3", "./main.py"]
# CMD ["./manage.py", "runserver", "0.0.0.0:8000"]


# FROM python:3.9-slim-buster
# WORKDIR /app
# COPY --from=poetry /app/requirements.txt .
# RUN pip install -r requirements.txt
# COPY . .
# CMD ["./manage.py", "runserver", "0.0.0.0:8000"]



# syntax=docker/dockerfile:1

# COPY requirements.txt requirements.txt
# RUN pip3 install -r requirements.txt
