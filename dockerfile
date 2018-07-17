FROM python:3.6.4
EXPOSE 5757
ADD requirements.txt /app/requirements.txt
ADD ./KNN/ /app/
WORKDIR /app/
RUN pip install -r requirements.txt
#CMD ["/bin/bash"]
ENTRYPOINT celery -A KNN worker --concurrency=20 --loglevel=debug --settings=celery