import os
from flask import Flask ,render_template
from flask_login import login_required, login_user, logout_user, current_user, LoginManager
from db import db
from model import User ,produto
from flask import Blueprint
from Blueprints.registrar.registrar import registrar_bp
from Blueprints.login.login import login_bp
from Blueprints.compras.compras import compras_bp
import hashlib

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.store-clean'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
UPLOAD_FOLDER = os.path.join(app.root_path, 'static', 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


db.init_app(app)
app.secret_key = 'davicvl'

login_manager = LoginManager()
login_manager.init_app(app)

login_manager.login_view = 'login.login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

app.register_blueprint(registrar_bp)
app.register_blueprint(login_bp)
app.register_blueprint(compras_bp)

@app.route('/')
def home():
    return render_template('home.html')

 with app.app_context():
        db.create_all()
