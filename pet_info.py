def coletar_nome_pet(nome):
    return nome

def coletar_idade_pet(idade_str):
    try:
        idade = int(idade_str)
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        return idade
    except ValueError:
        raise ValueError("Por favor, insira um número válido para a idade.")

def coletar_peso_pet(peso_str):
    try:
        peso = float(peso_str)
        if peso < 0:
            raise ValueError("O peso não pode ser negativo.")
        return peso
    except ValueError:
        raise ValueError("Por favor, insira um número válido para o peso.")

def mostrar_dados_pet(nome, idade, peso):
    return {
        "nome": nome,
        "idade": idade,
        "peso": peso
    }