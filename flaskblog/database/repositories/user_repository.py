from flaskblog import db
from flaskblog.database.repositories.base_repository import IRepository
from flaskblog.models.user import User

class UserRepository(IRepository):
    def get_by_username(username):
        return User.query.filter_by(username=username).first()

    def get_by_email(email):
        return User.query.filter_by(email=email).first()

    def get_by_id(id):
        return User.query.get(int(id))

