FROM python:3.6.4
EXPOSE 5757
ADD requirements.txt /app/requirements.txt
ADD ./knn/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
ENTRYPOINT celery -A knn worker --concurrency=20 --loglevel=debug
