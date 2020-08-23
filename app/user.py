from app import app, db, login_manager
import bcrypt
from flask_login import UserMixin

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return f"User({self.username})"

    def set_password(self, password):
        encoded = password.encode()
        if len(encoded) > 72:
            app.logger.warning(
                "`bcrypt` has a password lenght limit of 72 characters, characters \
                beyond that will be ignored"
            )
        self.password_hash = bcrypt.hashpw(encoded, bcrypt.gensalt())

    def check_password(self, password):
        encoded = password.encode()
        return bcrypt.hashpw(encoded, self.password_hash)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
