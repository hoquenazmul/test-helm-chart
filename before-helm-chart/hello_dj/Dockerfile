FROM python:3.11-alpine
WORKDIR /app
ENV PAGE_TITLE='Hello DJ World'
ENV BG_COLOR=darkblue
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 8000
COPY . .
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]