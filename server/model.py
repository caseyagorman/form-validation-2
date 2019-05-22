from flask_sqlalchemy import SQLAlchemy
# import sqlalchemy
db = SQLAlchemy()
# def db as instance of sqlalchemy



class User(db.Model):
    # define user class, inherits from SQLAlchemy.Model
    __tablename__ = "users"
    id = db.Column(db.Integer,
                   autoincrement=True,
                   primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(25), nullable=False)
    password = db.Column(db.String(128), nullable=False)



def connect_to_db(app):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///form'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.app = app
    db.init_app(app)

if __name__ == "__main__":
    from server import app
    connect_to_db(app)