import os
from flask import Flask ,render_template, redirect
from flask_login import login_required, LoginManager
from db import db
from model import User ,produto
from Blueprints.registrar.registrar import registrar_bp
from Blueprints.login.login import login_bp
from Blueprints.compras.compras import compras_bp
from Blueprints.compras.compras import pagamento_bp
import cloudinary.uploader
from dotenv import load_dotenv
load_dotenv()


app=Flask(__name__)


cloudinary.config(
    cloud_name=os.getenv("CLOUDINARY_CLOUD_NAME"),
    api_key=os.getenv("CLOUDINARY_API_KEY"),
    api_secret=os.getenv("CLOUDINARY_API_SECRET")
)

database_url = os.getenv("DATABASE_URL")

if database_url:
    if database_url.startswith("postgres://"):
        database_url = database_url.replace("postgres://", "postgresql://", 1)

    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
else:
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///trabalho.db"

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
app.register_blueprint(pagamento_bp)

@app.route('/')
def home():
    return render_template('home.html')
@app.route("/admin/produtos")
@login_required
def admin():
    produtos = produto.query.all()
    return render_template("admin_produtos.html", produtos=produtos)

@app.route('/deletar/<int:produto_id>')
@login_required
def deletar(produto_id):
    prod = produto.query.get(produto_id)

    if prod:
        db.session.delete(prod)
        db.session.commit()

    return redirect("/admin/produtos")


if __name__ == "__main__":
    app.run(debug=True)