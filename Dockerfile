FROM python:3-onbuild

ENV PYTHONUNBUFFERED=1

COPY start.sh /start.sh

EXPOSE 8000

ADD . /code/

#CMD ["/start.sh"]
