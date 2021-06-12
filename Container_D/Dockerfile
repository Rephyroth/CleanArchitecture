FROM python:3

COPY . /usr/src/Container_D

WORKDIR /usr/src/Container_D

RUN pip install --no-cache-dir -r requirements.txt

CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]

