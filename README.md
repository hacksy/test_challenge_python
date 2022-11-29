# Product Management with FastAPI-Python


## Description

_Test to manage products using Python without Flask_

This test uses Clean Architecture to create n layers for differents structures (domain / data and presentation plus DI ) to 
created endpoints to list / add / retrieve and update a product.
Includes fetching random values for discount, cache-ing using lru_cache based on id / status (Doesnt really make it a lot faster) and logs 
all requests inside logger.txt files with the duration of each request
Logs are generated in the file logger.txt

## Installation

- Install all dependencies

  ```sh
  $ pipenv install --dev
  ```

- Run the application:

  ```sh
  $ pipenv run uvicorn main:app --reload
  ```
- To access the api go to `localhost:8000`

-  To access the documentation , go to  `localhost:8000/redoc` for OpenAPI Documentation
-  To access the documentation , go to  `localhost:8000/docs` for Swagger Documentation
- 
## Testing

For Testing, you can run
  ```sh
  $ pipenv run pytest
  ```
