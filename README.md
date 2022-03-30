# NewsBoard

A fully functional REST API for creating posts, and comments on them. The API is deployed [here](https://news1board.herokuapp.com/). 

Refer to https://bit.ly/3qNe6bm for brief documentation.

## Usage

Clone the repo, make sure config files are set-up properly, then pull the repo at https://dockr.ly/3Lj2d4K to access the images and run
```python
docker-compose build
docker-compose up
```
You may have to trigger the background-task executor *Huey* only for development (local) mode by
```python
manage.py run_huey
```
