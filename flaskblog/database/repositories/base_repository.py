from flaskblog import db

class IRepository(object):
    def create(db_model):
        db.session.add(db_model)
        db.session.commit()

    def delete(db_model):
        pass

    def get_by_id(db_model):
        pass

    def update(db_model):
        pass
