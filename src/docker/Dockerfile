FROM python:3.11

# install Python 3 and libraries
RUN apt-get update && apt-get install -y python3 python3-pip

# WORKDIR /src/
# RUN python3 -m venv tips-env
# RUN source ./tips-env/bin/activate

RUN pip3 install pymongo==4.3.*
RUN pip3 install "fastapi[all]"
RUN pip3 install pytest==7.2.*
RUN pip3 install "uvicorn[standard]"

WORKDIR /src/
COPY . .

# install app as python package
WORKDIR /src/tips-app/
# RUN pip3 install -e .

# run tests
# RUN cd Infrastructure/Tests
# RUN pytest

# start server with API
CMD ["uvicorn", "Infrastructure.Controllers.api:app", "--proxy-headers", "--reload", "--host", "0.0.0.0", "--port", "8000"]