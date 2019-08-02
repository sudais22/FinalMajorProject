FROM python:2.7.16

EXPOSE 8888

RUN mkdir -p /usr/src/app

WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . .


ENTRYPOINT ["python", "rest2.py"]

