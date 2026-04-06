from fastapi import FastAPI
from models import User, Post, Comment
from database import users, posts, comments

app = FastAPI()

@app.get("/users")
def get_users(page: int = 1, page_size: int = 5):
    start = (page - 1) * page_size
    end = start + page_size
    return users[start:end]

@app.post("/users")
def create_user(user: User):
    users.append(user)
    return user

@app.put("/users/{user_id}")
def update_user(user_id: int, updated: User):
    for i, u in enumerate(users):
        if u.id == user_id:
            users[i] = updated
            return updated
    return {"error": "User not found"}

@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    for u in users:
        if u.id == user_id:
            users.remove(u)
            return {"message": "Deleted"}
    return {"error": "User not found"}

@app.get("/posts")
def get_posts():
    return posts

@app.post("/posts")
def create_post(post: Post):
    posts.append(post)
    return post

@app.get("/comments")
def get_comments():
    return comments

@app.post("/comments")
def create_comment(comment: Comment):
    comments.append(comment)
    return comment

@app.get("/users/{user_id}")
def get_user_with_posts(user_id: int):
    for u in users:
        if u.id == user_id:
            u.posts = [p for p in posts if p.user_id == user_id]
            for p in u.posts:
                p.comments = [c for c in comments if c.post_id == p.id]
            return u
    return {"error": "User not found"}