from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from pet_info import coletar_nome_pet, coletar_idade_pet, coletar_peso_pet, mostrar_dados_pet

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pets.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(50), nullable=False)
    idade = db.Column(db.Integer, nullable=False)
    peso = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f'<Pet {self.nome}>'

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        try:
            idade = coletar_idade_pet(request.form['idade'])
            peso = coletar_peso_pet(request.form['peso'])
        except ValueError as e:
            return render_template('index.html', error=str(e), pets=Pet.query.all())

        novo_pet = Pet(nome=nome, idade=idade, peso=peso)
        db.session.add(novo_pet)
        db.session.commit()

        return render_template('index.html', pet_info=novo_pet, pets=Pet.query.all())

    return render_template('index.html', pets=Pet.query.all())

if __name__ == '__main__':
    app.run(debug=True)