from flaskblog import User

# Print all users
User.query.all()

# Print first user
User.query.first()

# Filter users by username
User.query.filter_by(username='u1').all()

# Get by user id
User.query.get(1)




# Create posts
# post1 = Post(title='post1', content='content for post #1')
