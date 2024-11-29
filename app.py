# 1. Crie um dicionário
pessoas = {}

# 2. Adicione as pessoas
pessoas["Alice"] = 30
pessoas["Bob"] = 25
pessoas["Charlie"] = 35

# 3. Mostre as informações
for nome, idade in pessoas.items():
    print(f"Nome: {nome}, Idade: {idade}")