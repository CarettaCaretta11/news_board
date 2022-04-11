# NewsBoard

A fully functional REST API for creating posts, and comments on them. The API is deployed [here](https://news1board.herokuapp.com/api). 

Refer to https://bit.ly/3qNe6bm for the brief documentation.

## Usage

Clone the repo, make sure config files are set-up properly, then pull the repo at https://dockr.ly/3Lj2d4K to access the images and run
```python
docker-compose build
docker-compose up
```
For the development mode, to daily reset all the upvotes
```python
(python) manage.py run_huey
```
For the production, upvotes are reset at 6.30 P.M. (UTC) everyday.
