This is COMP9900 project backend for group 44:

## Request packages:
python3
Flask
Jinja2
Flask-RESTful
jsonschema
six
sqlite3

#Running environments:
Docker

#How to run:
Run docker

For Service1:
docker build -t Service1 .

docker run -p 8080:5000 -t Service1
//run this service on port 8080

For Service2:
docker build -t Service2 .

//docker run -p 8081:5000 -t Service2
//run this service on port 8081

