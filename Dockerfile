FROM python:3.8
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
RUN pip install python-dotenv
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]