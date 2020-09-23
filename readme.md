# Simple prediction server with ipynb

## Features
* http server
* use .ipynb
* container

## environoments
* Docker version 19.03.8

## How to start this
1. Build and run docker image
   ```sh
   docker-compose up -d
   ```
2. Try to post 
   `http://localhost:8000`
   ```json
   {
       "sepal length (cm)":1,
       "sepal width (cm)":2,
       "petal length (cm)":3,
       "petal width (cm)":4
    }
   ```
