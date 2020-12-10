FROM python
WORKDIR /src
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY ./src /src
EXPOSE 5000
CMD python server.py
 