FROM python:3

# install Python 3 and libraries
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pymongo
RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"

WORKDIR /app
COPY infrastructure/server.py ./
RUN python3 server.py


EXPOSE 27017
