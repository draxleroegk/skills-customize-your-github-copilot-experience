# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build a simple REST API using FastAPI by creating endpoints, validating request data, and returning consistent JSON responses.

## 📝 Tasks

### 🛠️ Create Your First FastAPI Endpoints

#### Description
Set up a FastAPI application and implement basic endpoints to check server health and list available books.

#### Requirements
Completed program should:

- Create a FastAPI app instance in `starter-code.py`.
- Implement `GET /` that returns a welcome JSON message.
- Implement `GET /health` that returns `{ "status": "ok" }`.
- Implement `GET /books` that returns a list of book objects from in-memory data.


### 🛠️ Add POST Endpoint with Validation

#### Description
Create an endpoint to add a new book and validate incoming data using a Pydantic model.

#### Requirements
Completed program should:

- Define a `BookCreate` model with `title`, `author`, and `year` fields.
- Implement `POST /books` that accepts JSON input matching `BookCreate`.
- Add a generated `id` for each new book and store it in memory.
- Return the created book with HTTP status `201`.


### 🛠️ Build Single-Resource Routes and Error Handling

#### Description
Implement routes to read and delete a specific book by ID and return clear errors when the book does not exist.

#### Requirements
Completed program should:

- Implement `GET /books/{book_id}` to return one book by ID.
- Implement `DELETE /books/{book_id}` to remove a book and return a confirmation message.
- Return HTTP `404` with a helpful error message when `book_id` is not found.
- Include at least one example request/response in comments or a short markdown note.
