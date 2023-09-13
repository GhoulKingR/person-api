# Person API

Currently this API is hosted publicly in this domain: https://person-api-uied.onrender.com/api

## Running this project locally

To run this application, you'll need to have [Pipenv](https://pipenv.pypa.io/en/latest/installation/) installed on your machine, and a [MongoDB](https://www.mongodb.com/docs/manual/tutorial/getting-started/) [connection string](https://www.mongodb.com/docs/drivers/node/current/quick-start/create-a-connection-string/) to your database.

Once you have everything ready, follow these steps to get this application running:

First, create a `.env` file in the root of this project.

Next, save your MongoDB connection string to `MONGO_SERVER` in the `.env` file:

```env
MONGO_SERVER="mongodb+srv://connection.string/to?mongodb=database"
```

Then, set up this project's virtual environment on your system with this command:

```bash
pipenv shell
```

Finally, run the app with this command:

```bash
python main.py
```

Python will host the application in `http://127.0.0.1:5000` by default.

## What next?

You can take a look into the [DOCUMENTATION.md](/DOCUMENTATION.md) file to understand that endpoints that this API provides and how they work. You can also take a look at the [UML Diagram](/UML%20Diagram.png) of this application.
