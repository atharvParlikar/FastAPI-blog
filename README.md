# Welcome Zenskar Team

This is just a small project i scraped togeather using FastAPI as it is in your tech stack.
This is just to show that i have the knowledge of REST architecture and I am decent at making web APIs.
It uses `sqlite` with `peewee ORM`

## Installation
To get started follow the instructions 👇

1. Clone the repo and navigate to the directory
```bash
git clone https://github.com/atharvParlikar/FastAPI-blog && cd FastAPI-blog
```

2. Install dependencies
```bash
pip3 install -r requirements.txt
```

3. Run the server
```bash
uvicorn main:app --reload
```

## Endpoints

The API has following Endpoints

### POST /blogs
Creates a new blog post

**Request body**:
```json
{
    "title": "My First Blog Post",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
}
```

**Response**
```json
{
    "id": 1
}
```

### GET /blogs/{blog_id}

Retrieves a single blog post by ID.

**path parameters**:
- `blog_id`: The ID of the blog post to retrieve.

**Response**:
On success, returns a JSON object containing the ID, title, and content of the blog post.
```json
{
    "id": 1,
    "title": "My First Blog Post",
    "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
}
```

### GET /getBlogs
Retrieves all blog posts.

**Response**:
On success, returns a JSON object containing a list o all blog posts.
```json
{
    "blogs": [
        {
            "id": 1,
            "title": "My First Blog Post",
            "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit."
        },
        {
            "id": 2,
            "title": "My Second Blog Post",
            "content": "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
        }
    ]
}
```

### PUT /blogs/{blog_id}
Updates a blog post by ID.

**Path Parameters**:
- `blog_id`: Id of blog to be updated

**Request Body**:
The request body must be a JSON object containing one or both of the following fields:
- `title`: The new title of blog post.
- `content`: The new content of the blog post.

```json
{
    "title": "My Updated Blog Post"
}
```

**Responses**:
```json
{
    "status": "done"
}
```

### DELETE   /blogs/{blog_id}
Deletes a blog post using blog_id

**path parameters**:
- `blog_id`: The ID of the blog post to retrieve.

**Response**:
```json
{
    "status": "done"
}
```
