from app import app, db
from app.models import User, Post

# creates a shell context that adds the database instance and models to the shell session:
# so that we dont have to type >>> from app import db and
# >>> from app.models import User, Post from the linux SHELL every time!!
# update this as the database and models grow

@app.shell_context_processor
def make_shell_context():
    return {"db": db, "User": User, "Post": Post}