from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///update_manager.db'
db = SQLAlchemy(app)

# Modelo para Clientes
class Cliente(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)
    sistema = db.Column(db.String(100), nullable=False)

# Modelo para Analistas
class Analista(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(100), nullable=False)

# Modelo para Atualizações
class Atualizacao(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cliente_id = db.Column(db.Integer, db.ForeignKey('cliente.id'), unique=True, nullable=False)
    analista_id = db.Column(db.Integer, db.ForeignKey('analista.id'), nullable=True)
    status = db.Column(db.String(50), default='Pendente')
    data_conclusao = db.Column(db.DateTime, nullable=True)
    cliente = db.relationship('Cliente', backref=db.backref('atualizacao', uselist=False, lazy=True))
    analista = db.relationship('Analista', backref=db.backref('atualizacoes', lazy=True))

@app.route('/')
def index():
    filtro = request.args.get('filtro', 'todos')
    if filtro == 'pendentes':
        atualizacoes = Atualizacao.query.filter_by(status='Pendente').all()
    elif filtro == 'andamento':
        atualizacoes = Atualizacao.query.filter_by(status='Em andamento').all()
    elif filtro == 'pausado':
        atualizacoes = Atualizacao.query.filter_by(status='Pausado').all()
    elif filtro == 'concluido':
        atualizacoes = Atualizacao.query.filter_by(status='Concluído').all()
    else:
        atualizacoes = Atualizacao.query.all()

    clientes = Cliente.query.all()
    analistas = Analista.query.all()
    return render_template('index.html', clientes=clientes, analistas=analistas, atualizacoes=atualizacoes, filtro=filtro)

@app.route('/add_cliente', methods=['POST'])
def add_cliente():
    nome = request.form.get('nome')
    sistema = request.form.get('sistema')
    if nome and sistema:
        novo_cliente = Cliente(nome=nome, sistema=sistema)
        db.session.add(novo_cliente)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/add_analista', methods=['POST'])
def add_analista():
    nome = request.form.get('nome')
    if nome:
        novo_analista = Analista(nome=nome)
        db.session.add(novo_analista)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/atribuir_atualizacao', methods=['POST'])
def atribuir_atualizacao():
    cliente_id = request.form.get('cliente_id')
    analista_id = request.form.get('analista_id')
    if cliente_id and analista_id:
        nova_atualizacao = Atualizacao(cliente_id=cliente_id, analista_id=analista_id, status='Pendente')
        db.session.add(nova_atualizacao)
        db.session.commit()
    return redirect(url_for('index'))

@app.route('/atualizar_status/<int:att_id>', methods=['POST'])
def atualizar_status(att_id):
    novo_status = request.form.get('status')
    atualizacao = Atualizacao.query.get(att_id)
    if atualizacao and novo_status in ['Pendente', 'Em andamento', 'Pausado', 'Concluído']:
        atualizacao.status = novo_status
        atualizacao.data_conclusao = datetime.now() if novo_status == 'Concluído' else None
        db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
