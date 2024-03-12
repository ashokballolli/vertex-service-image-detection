FROM python:3.11

RUN python3 -m pip install --upgrade pip

WORKDIR /ws

COPY requirements.txt /ws/

COPY app/ /ws/

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "app.py" ]