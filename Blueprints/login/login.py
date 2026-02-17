from  flask import Blueprint
from db import db
from werkzeug.security import check_password_hash
from model import User
from flask import render_template ,request ,redirect,url_for
from flask_login import login_user,logout_user,login_required,login_manager
login_bp = Blueprint('login', __name__, template_folder='templates1')

@login_bp.route('/login',methods=['GET','POST'])
def login():
    if request.method == 'GET':

       return render_template('login.html',)
    elif request.method == 'POST':

        nome = request.form['nomeForm']
        senha = request.form['senhaForm']

    user = User.query.filter_by(nome = nome).first()

    if not user or not check_password_hash(user.senha, senha):
        return redirect(url_for('login.login_erro'))


    login_user(user)
    return redirect(url_for('home'))
@login_bp.route('/login erro')
def login_erro():
    return render_template('/login erro.html')





