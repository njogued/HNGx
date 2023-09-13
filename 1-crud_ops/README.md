### Django REST API

- The API is a CRUD operations API where:

```
CREATE - POST Request
READ - GET Request
UPDATE - PUT Request
DELETE - DELETE Request
```

#### Endpoints

CREATE => /api - Add new person  
READ => /api/user_id - Fetch new person details
UPDATE => /api/user_id - Modify existing details  
DELETE => /api/user_id - Remove a person

#### Example Usage

#### Notes for Devs

To run the api on your local machine:

- Install django
- Install django rest framework
- Run `py manage.py runserver`
- Access the api using localhost on port 8000
