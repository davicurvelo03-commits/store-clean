from flask import blueprints
from flask import render_template , request
from model import User
from db import db
from model import produto

compras_bp = blueprints.Blueprint('compras', __name__, template_folder='templates.compra')

@compras_bp.route('/compras',methods=['GET','POST'])
def compras():
    produtos = produto.query.all()
    return render_template('compras.html', produtos = produtos)