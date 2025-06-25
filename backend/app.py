from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
import os

app = Flask(__name__)
CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL")
app.config["JWT_SECRET_KEY"] = "super-secret"
db = SQLAlchemy(app)
jwt = JWTManager(app)

from models import User
from routes import auth_routes

app.register_blueprint(auth_routes)

@app.route('/')
def index():
    return {"message": "Cyber Defense Lab Backend Running"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
```

---

### 🧠 backend/models.py
```python
from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    role = db.Column(db.String(10), nullable=False)  # red or blue
```

---

### 🧠 backend/routes.py
```python
from flask import Blueprint, request, jsonify
from app import db
from models import User
from flask_jwt_extended import create_access_token

auth_routes = Blueprint("auth", __name__)

@auth_routes.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    user = User(username=data["username"], password=data["password"], role=data["role"])
    db.session.add(user)
    db.session.commit()
    return jsonify(msg="User registered"), 201

@auth_routes.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()
    if user and user.password == data["password"]:
        token = create_access_token(identity={"username": user.username, "role": user.role})
        return jsonify(access_token=token)
    return jsonify(msg="Bad credentials"), 401