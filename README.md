## About Repo

Rest API with microservice architecture with following apis:


- Security

CRUD behavior for Users, the user information is stored MongoDB.

Endpoints in the api:

| EndPoint | Description | Input | Output |
| ------ | ------ | ------ | ------ |  
| GeAll | Endpoint returns a user list |  | { data: [{userId, name, email, password, isActive:true}, {userId, name, email, password, isActive:false}], responseCode , message} |
| GetAllActive | Endpoint returns an active user list (where isActive=true) |  | {data:[{userId, name, email, password, isActive:true}], responseCode , message} |
| Create | Endpoint to insert a new user. Backend needs to create the userId and isActive as default value |  | {data:{userId, name, email, password, isActive:true}, responseCode , message} |
| Update | Endpoint to update an especific user. | {userId, name, email, password, isActive} | {data:{userId, name, email, password, isActive}, responseCode , message} |
| Delete | Endpoint to delete an user | userId | { data: {userId:""}, responseCode , message} |

- Book

Endpoints for searching a book (request to another api).

| EndPoint | Description | Input | Output | Request | Example
| ------ | ------ | ------ | ------ | ------ | ------ |   
| GetByTitle | Endpoint that returns the info of a book. | title | { data: {title, author:["A", "B"], key, place:["A","B"]}, responseCode , message} | http://openlibrary.org/search.json?title={title} | http://openlibrary.org/search.json?title=The_Way_of_All_Flesh |
| GetByKey | Endpoint that returns the details of a book | key | { data: {title, description, covers, subjects:["A", "B"], latestRevision}, responseCode , message} | https://openlibrary.org/works/{key}.json | https://openlibrary.org/works/OL15099863W.json |



## Things to consider them:

- create virtual env: python3 python3 -m venv venv
- run pip3 install -r requirements.txt
- create .env file with environment variable with connection strings, DBNm and others.
- If you are using vs code, go to run and debug and create a launch.json file and add the following (for env file, copy your path and paste it): { "version": "0.2.0", "configurations": [ { "name": "Python: Current File", "type": "python", "request": "launch", "program": "./app.py", "console": "integratedTerminal", "envFile": "/Users//Desktop/BOOKING_APP/space-booking-api/Management_API/.env" } ] }
 - Run the project under 'Run and debug'


### If you get mongo issues:
- certificate: Run the following command with the proper python version on your system: open "/Applications/Python 3.10/Install Certificates.command"
- Enable network configuration in Mongo Atlas
- Remove any ssl flag in connectionstring.
