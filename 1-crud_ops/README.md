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

Note: The person resource has two attributes: the person name and ID

#### Example Usage

On Linux Terminal:  
GET (all) => curl wget https://crudopsapi.onrender.com/api  
GET (one) => curl -X GET https://crudopsapi.onrender.com/api/<user:id>

POST => curl -X POST -H "Content-Type: application/json" -d '{"key": "value"}' https://crudopsapi.onrender.com/api/  
PUT => curl -X PUT -H "Content-Type: application/json" -d '{"key": "value"}' https://crudopsapi.onrender.com/api/<user:id>  
DELETE => curl -X DELETE https://crudopsapi.onrender.com/api/<user:id>

On POSTMAN: [RTFM](https://learning.postman.com/docs/getting-started/first-steps/sending-the-first-request/#:~:text=Postman%20enables%20you%20to%20create,response%20appears%20right%20inside%20Postman.)

#### Notes for Devs

To run the api on your local machine:

- Install django
- Install django rest framework
- Run `py manage.py runserver`
- Access the api using localhost on port 8000
