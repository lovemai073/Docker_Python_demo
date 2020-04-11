FROM python:3
MAINTAINER Albertcc

WORKDIR /app

ADD . /app
#Install Cron
RUN pip install -r requirements.txt

EXPOSE 80

ENV NAME=World
# Run the command on container startup
CMD ["python","-u","app.py"]










