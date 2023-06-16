from init import db, ma

class User(db.model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primaruy_key=True)
    name = db.Column(db.String(50))
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)

class UserSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'email', 'password', 'is_admin')

user_schema = UserSchema(exclude=['password'])
user_schema = UserSchema(many=True, exclude=['password'])

