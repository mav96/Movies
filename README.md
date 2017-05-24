# REST API for movies

## Docs:
* [Task](https://drive.google.com/file/d/0B5e-E0vLwQkNT3FPdUVfY2UzYVk/view?usp=sharing)
* [Explanatory note](https://docs.google.com/document/d/1NoKbG3W6_l0PWpwXr587dSaH0EYNZkl7TWTL2ANfaAg/edit?usp=sharing)

## Install:
```
git clone https://github.com/mav96/Movies.git
cd Movies
docker-compose build
docker-compose run webapp python3 manage.py check
docker-compose run webapp python3 manage.py migrate
```
## Setup limits for CPU and MEM:
Chenge limits for nodes in docker-compose.yml.
See [Runtime constraints on resources](https://docs.docker.com/engine/reference/run/#runtime-constraints-on-resources)


## Start for 3 nodes:
```
docker-compose up --scale webapp=3 -d
```


## Test:
* Install httpie (instead curl)
```
	apt-get install httpie
```

* Upload movies list
```
	http PUT http://localhost/put/movies.json < DATA/movies.json
```
* Save films statistic
```
	http PUT http://localhost/stats/stats.csv < DATA/stats.csv
```
* Get statistic
```
http GET http://localhost/movies
```

### Links:

 * [Django REST framework](http://www.django-rest-framework.org/)
 * [Docker-compose](https://docs.docker.com/compose/django/)
 * [A sample Docker workflow with Nginx](http://anandmanisankar.com/posts/docker-container-nginx-node-redis-example/)
 * [How to scale Docker Containers with Docker-Compose](https://www.brianchristner.io/how-to-scale-a-docker-container-with-docker-compose/)
 * [A command line HTTP client](https://httpie.org/doc)

