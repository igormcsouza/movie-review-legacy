This project was discontinued! A very Big one started then!! :) It is the MOVIE REVIEW PLUS.

On the new project we now have our Frontend, Backend and Package splitted to be easier to reproduce it latter!

You can find out more about the new project on those repositories:

https://github.com/igormcsouza/movie-review-plus-frontend
https://github.com/igormcsouza/movie-review-plus-backend
https://github.com/igormcsouza/movie-review-plus-package

# Text Sentiment Recognition Online

The idea is to implement a natural language processing model to classify wheter the review of a movie is Positive or Negative, then, load it online to get peoples review and classify it.

## Push containers to Heroku

To push containers to production is very simple with heroku containers. Below is a very simple script to make it work properly! Remember to build the Docker image to production and let the docker-compose deal with the development environment.

    heroku container:login
    docker tag <image_name> registry.heroku.com/<app>/<process_name>
    docker push registry.heroku.com/<app>/<process_name>
    heroku container:release <process_name> -a <app>

I made an script to run the above commands quickly! Just type the bellow on the terminal.

    sh heroku.sh docker_movie_web smart-movie-review web

## Dataset

https://www.kaggle.com/luisfredgs/imdb-ptbr