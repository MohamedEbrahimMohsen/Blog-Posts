from flaskblog import db, User, Post

# Delete the current db
db.drop_all()

# Create db from scratch
db.create_all()

# Create users
user1 = User(username='user1', email='u1@gmail.com', password='password1')
user2 = User(username='user2', email='u2@gmail.com', password='password2')
user3 = User(username='user3', email='u3@gmail.com', password='password3')

# Add users to db
db.session.add(user1)
db.session.add(user2)
db.session.add(user3)

# Commit changes to db
db.session.commit()
