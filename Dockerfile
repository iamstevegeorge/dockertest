FROM python:3.7-slim 
COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080
ENTRYPOINT [ "python" ] 
CMD [ "cmd.py" ]  