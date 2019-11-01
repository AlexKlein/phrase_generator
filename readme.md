# App for getting random wiki theme with links over API

In this project I realized API with GET requests to getting wiki themes with page links.

## Docker

When you need to build docker with app, then you have to follow this steps:
1. `docker build -t wiki_page_chooser:latest .` - you will build image and load it to docker-machine;
2. `docker run --rm -d --net=host wiki_page_chooser:latest` - you will start app with united host of container and docker-machine;
3. `http://192.168.99.100/` - you will check how container was started.