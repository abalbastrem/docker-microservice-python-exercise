FROM python:3

# install Python 3 and libraries
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pymongo
RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"

# start server with API
WORKDIR /app
COPY infrastructure/api.py ./
CMD ["uvicorn", "api:app", "--proxy-headers", "--host", "0.0.0.0", "--port", "8000"]