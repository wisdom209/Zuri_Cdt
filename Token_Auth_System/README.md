# Basic Authentication API Using Express Js

This is a simple Express.js API for user authentication using JSON Web Tokens (JWT). It provides two main endpoints: one for user login and another for checking the authentication status. It uses a predefined set of credentials for testing purposes.

## Prerequisites

Before you start using this API, make sure you have the following installed:

- [Node.js](https://nodejs.org/): Ensure you have Node.js installed on your machine.

## Getting Started
 

## Endpoints

### 1. User Login

- **URL:** `/login`
- **Method:** POST
- **Request Body:**

  ```json
  {
    "username": "Gold123",
    "password": "password123"
  }
  ```

- **Response:**

  - `200 OK` on successful authentication with a JSON response containing a JWT token:

    ```json
    {
      "token": "your-jwt-token",
      "username": "YourUsername",
      "password": "YourPassword"
    }
    ```

  - `400 Bad Request` if any required fields are missing or if the credentials are invalid.

### 2. Check Authentication Status

- **URL:** `/`
- **Method:** GET
- **Headers:**

  Add an `Authorization` header with the JWT token obtained during login:

  ```http
  Authorization: Bearer your-jwt-token
  ```

- **Response:**

  - `200 OK` on successful authentication with a JSON response containing user details:

    ```json
    {
      "username": "YourUsername",
      "password": "YourPassword"
    }
    ```

  - `401 Unauthorized` if the `Authorization` header is missing, the token is invalid, or the credentials do not match.


## To try it out locally

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-repo.git
   ```

2. Navigate to the project directory:

   ```bash
   cd your-project-directory
   ```

3. Install the required dependencies:

   ```bash
   npm install
   ```

4. Create a `.env` file in the project root and set the following environment variables:

   - `PORT`: The port on which the server will run. Defaults to 4000 if not provided.
   - `JWT_SECRET`: The secret key used for JWT token generation and verification. A default value is provided for testing purposes.
   - `USERNAME`: The test username for authentication. Defaults to "Gold123".
   - `PASSWORD`: The test password for authentication. Defaults to "password123".

   Example `.env` file:

   ```env
   PORT=4000
   JWT_SECRET=your-secret-key
   USERNAME=your-username
   PASSWORD=your-password
   ```

5. Start the server:

   ```bash
   npm start
   ```


