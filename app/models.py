"""
Contains Databse model classes
"""

from hashlib import md5
from datetime import datetime
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db, login

class User(UserMixin, db.Model):
    """
    Represetns a system User
    """
    id = db.Column(db.Integer, primary_key=True) 
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(256))
    about_me = db.Column(db.String(140))
    last_seen = db.Column(db.DateTime, default=datetime.utcnow)
    posts = db.relationship('Post', backref='author', lazy='dynamic')

    def __repr__(self):
        return f'<User {self.username}, {self.email}>'
    
    def set_password(self, password):
        """
        Set password to generated password hash
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Check if password hash matches set password
        """
        current_app.logger.debug(f"Checking password {password}")
        return check_password_hash(self.password_hash, password)

    @staticmethod
    @login.user_loader
    def load_user(id_):
        """
        Return user base on id.
        """
        return User.query.get(int(id_))

    def avatar(self, size="80"):
        """
        Return Gravatar URL based on email
        """
        # Gravatar identifies the avatar by the MD5 of the email address, the hash is not used for security.
        digest = md5(self.email.lower().encode('utf-8'), usedforsecurity=False).hexdigest()
        url = f'https://www.gravatar.com/avatar/{digest}?d=retro&s={size}'
        current_app.logger.debug(f"Get gravatar {url}")
        return url

class Post(db.Model):
    """
    Represents a User Post
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140))
    body = db.Column(db.String(140))
    timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Post: {self.title}: {self.body} By user_id {self.user_id}>'
