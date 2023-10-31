# Under stress

Project that have been tested by [siege](https://github.com/JoeDog/siege)

### Run project

`docker-compose up --build`

### Run siege stress tests

Test creation EP:

`siege -c 100 -t 20s --content-type="application/json" 'http://localhost:8000/products/create/ POST {"title": "Some title"}'`

Test products list (paginated by 100):

`siege -c 100 -t 20s --content-type="application/json" 'http://localhost:8000/products/list/'`

Test product receive:

`siege -c 100 -t 20s --content-type="application/json" 'http://localhost:8000/products/1/'`

Test internet simulation:

`siege -c 100 -t 20s --content-type="application/json" -f siege_urls.txt -i`

### Tests stat

[google table](https://docs.google.com/spreadsheets/d/1hpmQt7bsSr-Ts6Jpb4znZKFZt1hYI11zgBH24KfZHuk/edit?usp=sharing)
