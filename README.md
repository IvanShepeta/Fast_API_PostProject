# FastAPI Post Project

A FastAPI-based web application for managing posts, featuring JWT authentication, PostgreSQL integration, and Pydantic validation.

## 🚀 Features

- **JWT Authentication**: Secure user login and token-based access.
- **Post Management**: Create, read, update, and delete posts.
- **User Registration**: Register new users with hashed passwords.
- **Database Integration**: PostgreSQL with SQLAlchemy ORM.
- **Pydantic Validation**: Ensure data integrity and type safety.
- **File Upload/Streaming**: Upload and stream files (images, videos).

## 🛠️ Technologies Used

- **Backend**: FastAPI
- **Database**: PostgreSQL
- **ORM**: SQLAlchemy
- **Authentication**: PyJWT
- **Validation**: Pydantic
- **Environment Management**: Python-dotenv


# This API  has 4 routes  

## 1) Post route

#### This route is reponsible for creating post, deleting post, updating post and Checkinh post

## 2) Users route

#### This route is about creating users and searching user by id

## 3) Auth route

#### This route is about login system

## 4) Vote route

 #### This route is about likes or vote system and this route contain code for upvote or back vote there is not logic about down vote

## After run this API you need a database in postgres 
Create a database in postgres then create a file name .env and write the following things in you file 

````
DATABASE_HOSTNAME = localhost
DATABASE_PORT = 5432
DATABASE_PASSWORD = passward_that_you_set
DATABASE_NAME = name_of_database
DATABASE_USERNAME = User_name
SECRET_KEY = 09d25e094faa2556c818166b7a99f6f0f4c3b88e8d3e7 
ALGORITHM = HS256
ACCESS_TOKEN_EXPIRE_MINUTES = 60

````

## 📦 Installation

1. Clone the repository:

```bash
git clone https://github.com/IvanShepeta/Fast_API_PostProject.git
cd Fast_API_PostProject
