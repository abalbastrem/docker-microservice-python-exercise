FROM python:3.10

# install Python 3 and libraries
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pymongo
RUN pip3 install fastapi
RUN pip3 install "uvicorn[standard]"

# start server with API
WORKDIR /app/
COPY . .
CMD ["uvicorn", "Infrastructure.api:app", "--proxy-headers", "--reload", "--host", "0.0.0.0", "--port", "8000"]