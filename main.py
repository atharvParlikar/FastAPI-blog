from fastapi import FastAPI, HTTPException
from peewee import *
from pydantic import BaseModel

app = FastAPI()
db = SqliteDatabase('blog.db')

# Blog model

class Blog(Model):
    title = CharField()
    content = TextField()

    class Meta:
        database = db

db.create_tables([Blog])


# Pydantic models

class BlogCreate(BaseModel):
    title: str
    content: str

class BlogRead(BaseModel):
    id: int
    title: str
    content: str

class BlogUpdate(BaseModel):
    title: str = None
    content: str = None


# API routes

@app.post('/blogs')
def create_blog(blog: BlogCreate):
    blog = Blog.create(**blog.dict())
    return {'id': blog.id}

@app.get('/blogs/{blog_id}')
def read_blog(blog_id: int):
    blog = Blog.get_or_none(id=blog_id)
    if blog is None:
        raise HTTPException(status_code=404, detail='Blog not found')
    return BlogRead.from_orm(blog)

@app.get("/getblogs")
def get_blogs():
    return {
                "blogs": [x.__data__ for x in Blog.select()]
            }

@app.put('/blogs/{blog_id}')
def update_blog(blog_id: int, blog: BlogUpdate):
    update_data = blog.dict(exclude_unset=True)
    updated_count = Blog.update(**update_data).where(Blog.id == blog_id).execute()
    if not updated_count:
        raise HTTPException(status_code=404, detail='Blog not found')
    return None

@app.delete('/blogs/{blog_id}')
def delete_blog(blog_id: int):
    deleted_count = Blog.delete().where(Blog.id == blog_id).execute()
    if not deleted_count:
        raise HTTPException(status_code=404, detail='Blog not found')
    return None
