# NewsBoard

A fully functional REST API for creating posts, and comments on them. The API is deployed [here](https://news1board.herokuapp.com/). 

Refer to https://bit.ly/3qNe6bm for brief documentation.

## Usage

Clone the repo, make sure config files are set-up properly, then pull the repo at https://dockr.ly/3Lj2d4K to access the images and run
```python
docker-compose build
docker-compose up
```
You may also want to reset the upvotes given to posts. For the development mode, this is done by
```python
(python) manage.py run_huey
```
For the production, upvotes are reset at 6.30 P.M. (UTC) everyday.
