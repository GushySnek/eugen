FROM python:3.10
ADD main.py Home/jacque/eugen-master/eugen/ 
# TO DO trouver la bonne URL pour le raspberry
RUN pip install poetry
WORKDIR Home/jacque/eugen-master/
COPY pyproject.toml poetry.lock .
RUN poetry export -f requirements.txt --output requirements.txt
RUN pip install -r /eugen/requirements.txt
CMD ["python","./main.py"]

# CMD ["./manage.py", "runserver", "0.0.0.0:8000"]


# FROM python:3.9-slim-buster
# WORKDIR /app
# COPY --from=poetry /app/requirements.txt .
# RUN pip install -r requirements.txt
# COPY . .
# CMD ["./manage.py", "runserver", "0.0.0.0:8000"]