FROM alpine:latest

RUN apk add --no-cache python3-dev
RUN pip3 install --upgrade pip

COPY ./app /service_epic1
WORKDIR /service_epic1

RUN pip3 install -r requirements.txt
EXPOSE 5000

WORKDIR /service_epic1/demo
ENTRYPOINT ["python3"]
CMD ["__init__.py"]
