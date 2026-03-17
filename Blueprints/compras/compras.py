from flask import blueprints
from flask import render_template , request
from model import produto

compras_bp = blueprints.Blueprint('compras', __name__, template_folder='templates.compra')
pagamento_bp = blueprints.Blueprint('pagamento', __name__, template_folder='templates.compra')
@compras_bp.route('/compras',methods=['GET','POST'])
def compras():
    produtos = produto.query.all()
    return render_template('compras.html', produtos = produtos)

@pagamento_bp.route('/pagamentos/<int:id>',methods=['GET','POST'])
def pagar(id):
    produtos_pagamento = produto.query.filter_by(id=id).first()
    if not produtos_pagamento:
        return "Produto não encontrado", 404
    return render_template('pagamento.html',produto=produtos_pagamento)