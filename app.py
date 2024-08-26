from flask import Flask, render_template, request
from pet_info import coletar_nome_pet, coletar_idade_pet, coletar_peso_pet, mostrar_dados_pet

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        try:
            idade = coletar_idade_pet(request.form['idade'])
            peso = coletar_peso_pet(request.form['peso'])
        except ValueError as e:
            return render_template('index.html', error=str(e))

        pet_info = mostrar_dados_pet(nome, idade, peso)
        return render_template('index.html', pet_info=pet_info)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)