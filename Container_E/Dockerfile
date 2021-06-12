FROM python:3

COPY . /usr/src/Container_E

WORKDIR /usr/src/Container_E

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]

