FROM python:3.13-slim

WORKDIR /AppCore

ADD . /AppCore

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

CMD ["python", "src/AppCore.py"]