def coletar_nome_pet():
    nome = input("Nome do pet: ")

def coletar_idade_pet():
    while True:
        try:
            idade = int(input("Idade do pet (em anos): "))
            if idade < 0:
                print("A idade não pode ser negativa. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para a idade.")

def coletar_peso_pet():
    while True:
        try:
            peso = float(input("Peso do pet (em kg): "))
            if peso < 0:
                print("O peso não pode ser negativo. Tente novamente.")
            else:
                break
        except ValueError:
            print("Por favor, insira um número válido para o peso.")

def mostrar_dados_pet(nome, idade, peso):
    print("\nInformações do pet:")
    print(f"Nome: {nome}")
    print(f"Idade: {idade} anos")
    print(f"Peso: {peso} kg")

def coletar_informacoes_pet():
    nome = coletar_nome_pet()
    idade = coletar_idade_pet()
    peso = coletar_peso_pet()
    mostrar_dados_pet(nome, idade, peso)

if __name__ == "__main__":
    coletar_informacoes_pet()