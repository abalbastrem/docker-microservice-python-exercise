FROM python:3.11

# install Python 3 and libraries
RUN apt-get update && apt-get install -y python3 python3-pip
RUN pip3 install pymongo==4.3.*
RUN pip3 install "fastapi[all]"==0.87.*
RUN pip3 install pytest==7.2.*
RUN pip3 install "uvicorn[standard]"==0.20.*

WORKDIR /src/
COPY . .

WORKDIR /src/tips-app/

# start server with API
CMD ["uvicorn", "Infrastructure.Controllers.api:app", "--proxy-headers", "--reload", "--host", "0.0.0.0", "--port", "8000"]