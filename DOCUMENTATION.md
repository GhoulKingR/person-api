# Person API

This is a documentation of all the API endpoints you’ll can access in this project. And error messages that can occur when using them.

For a more comprehensive guide on running this project locally on your machine, check this project’s [README](/README.md).

# Endpoints

## `POST` /api

**Description**:

    This endpoint allows you to add a new person in the database. The database then creates an ID for each person when they're added.

    The person's database ID is useful for interacting with that person's record in the database through other endpoints.

**Format**:

    Request:
        Content-Type: application/json
        Body:
            {
                “name”: “user name”
            }

    Response:
        Content-Type: application/json
        Body:
            {
                "id": "userid",
                "name": "user name"
            }

**Example**:

```JS
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "name": "Chigozie Oduah"
});

var requestOptions = {
  method: 'POST',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://person-api-uied.onrender.com/api", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Output**:

```JSON
{
    "id": "65000a1d0bee50a4b9cf7b98",
    "name": "Chigozie Oduah"
}
```

## `GET` /api

**Description:**

    This endpoint allows you to get a list of all the people stored in the database.

**Format**:

    Response:
        Content-Type: application/json
        Body:
            [
                {
                    “id”: “userid1”,
                    “name”: “username one”
                },
                {
                    “id”: “userid2”,
                    “name”: “username two”
                }
            ]

**Example**:

```JS
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("https://person-api-uied.onrender.com/api", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Output**:

```JSON
[
    {
        "id": "65000a1d0bee50a4b9cf7b98",
        "name": "Chigozie Oduah"
    }
]
```

## `GET` /api/:id

**Description**:

    This endpoint allows you to fetch the full details of a person using their database ID.

    When you're calling, replace ":id" with the person's database ID.

**Format**:

    Response:
        Content-Type: application/json
        Body:
            {
                “id”: “userid”,
                “name”: “user name”
            }

**Example**:

```JS
var requestOptions = {
  method: 'GET',
  redirect: 'follow'
};

fetch("https://person-api-uied.onrender.com/api/65000a1d0bee50a4b9cf7b98", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Output**:

```JSON
[
    {
        "id": "65000a1d0bee50a4b9cf7b98",
        "name": "Chigozie Oduah"
    }
]
```

## `DELETE` /api/:id

**Description**:

    This endpoint allows you to remove a person from the database.

    To delete a user with this endpoint, replace `:id` in the url routes with the person's database ID.

    The endpoint will respond with the removed person's name and ID.

**Format**:

    Response:
        Content-Type: application/json
        Body:
            {
                "id": "userid",
                "name": "user name"
            }

**Example**:

```JS
var requestOptions = {
  method: 'DELETE',
  redirect: 'follow'
};

fetch("https://person-api-uied.onrender.com/api/64ff2f2b86b8705b614cd120", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Output**:

```JSON
{
    "id": "64ff2f2b86b8705b614cd120",
    "name": "Emmanuel Oduah"
}
```

## `PUT` /api/:id

**Description**:

    This endpoint allows you to modify the name of a person using their database ID.

    When you're calling the endpoint, you need to pass an object. That object should contain the new name you want to set the person to, formatted as in the "Format" section.

    This endpoint will then respond with the new object stored in the database. The same database ID, and with the new name.

**Format**:

    Request:
        Content-Type: application/json
        Body:
            {
                “name”: “user name”
            }

    Response:
        Content-Type: application/json
        Body:
            {
                "id": "userid",
                "name": "user name"
            }

**Example**:

```JS
var myHeaders = new Headers();
myHeaders.append("Content-Type", "application/json");

var raw = JSON.stringify({
  "name": "Goku Black"
});

var requestOptions = {
  method: 'PUT',
  headers: myHeaders,
  body: raw,
  redirect: 'follow'
};

fetch("https://person-api-uied.onrender.com/api/65000a1d0bee50a4b9cf7b98", requestOptions)
  .then(response => response.text())
  .then(result => console.log(result))
  .catch(error => console.log('error', error));
```

**Output**:

```JSON
{
    "id": "65000a1d0bee50a4b9cf7b98",
    "name": "Goku Black"
}
```
