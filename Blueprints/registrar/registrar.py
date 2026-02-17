
from flask import blueprints
import os
from werkzeug.utils import secure_filename
from flask import render_template , request ,redirect ,url_for ,current_app
from model import User
from db import db
from werkzeug.security import generate_password_hash
from model import produto
from flask_login import LoginManager , login_required

registrar_bp = blueprints.Blueprint('registrar', __name__, template_folder='templates registrar')

@registrar_bp.route('/registrar',methods=['GET','POST'])
def registrar():
    if request.method == 'GET':
        return render_template('registrar.html', )
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        senha = request.form['senhaForm']

        senha_hash = generate_password_hash(senha)

        novo_User = User(nome=nome, senha=senha_hash)
        db.session.add(novo_User)
        db.session.commit()

    return redirect(url_for('login.login'))
@registrar_bp.route('/registrar-produtos',methods=['GET','POST'])
@login_required
def registrar_produtos():


    if request.method == 'GET':
        return render_template('rg.produtos.html')
    elif request.method == 'POST':
        nome = request.form['nomeForm']
        descricao = request.form['descricaoForm']
        preco = request.form['precoForm']
        quantidade = request.form['quantidadeForm']
        imagem = request.files['imagemForm']

        if imagem and imagem.filename != '':
            nome_arquivo = secure_filename(imagem.filename)
            caminho = os.path.join('static/uploads', nome_arquivo)
            imagem.save(caminho)
            nome_imagem = nome_arquivo
        else:
            nome_imagem ='default.jpg'

        novo_produto = produto(nome=nome, descricao=descricao, preco=preco, quantidade=quantidade, imagem=nome_imagem)
        db.session.add(novo_produto)
        db.session.commit()

    return redirect(url_for('compras.compras'))
