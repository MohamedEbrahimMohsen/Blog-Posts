from flaskblog import login_manager
from flaskblog.database.repositories.user_repository import UserRepository

@login_manager.user_loader
def load_user(user_id):
    UserRepository.get_by_id(user_id)