from pydantic import BaseModel
from typing import List, Optional

class Comment(BaseModel):
    id: int
    text: str
    post_id: int

class Post(BaseModel):
    id: int
    title: str
    user_id: int
    comments: List[Comment] = []

class User(BaseModel):
    id: int
    name: str
    posts: List[Post] = []