Build the docker images
$ docker build -t my-flask -f Dockerfile-flask .
$ docker build -t my-nginx -f Dockerfile-nginx .

Create a network link
$ docker network create my-network

Run flask
$ docker run --name flask --net my-network -v "$(pwd):/app" --rm my-flask

Run nginx
$ docker run --name nginx --net my-network -p "80:80" --rm my-nginx
