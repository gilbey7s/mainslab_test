FROM python:3.7-slim
WORKDIR /project
COPY requirements.txt /project
RUN pip3 install -r requirements.txt --no-cache-dir
COPY . /project
RUN python3 manage.py migrate
CMD ["python3", "manage.py", "runserver", "0:8000"]