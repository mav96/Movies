# Movies
REST API for movies


# Install
git clone https://github.com/mav96/Movies.git
cd Movies
docker-compose build
docker-compose run webapp python3 manage.py check
docker-compose run webapp python3 manage.py migrate
docker-compose up --scale webapp=3 -d


apt-get install httpie
http PUT http://localhost/put/file < DATA/movies.json
http PUT http://localhost/stats/file < DATA/stats.csv
http GET http://localhost/movies

