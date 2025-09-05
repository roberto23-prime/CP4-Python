import json
import os

# Arquivo para armazenar os dados do estoque
ARQUIVO_DADOS = "estoque.json"

# Carrega o estoque do arquivo ou cria um vazio
def carregar_estoque():
    if os.path.exists(ARQUIVO_DADOS):
        with open(ARQUIVO_DADOS, 'r') as arquivo:
            return json.load(arquivo)
    return {}

# Salva o estoque no arquivo
def salvar_estoque(estoque):
    with open(ARQUIVO_DADOS, 'w') as arquivo:
        json.dump(estoque, arquivo, indent=4)

# Adiciona um novo produto
def adicionar_produto(estoque):
    print("\n=== Adicionar Novo Produto ===")
    codigo = input("Digite o código do produto (único): ")
    if codigo in estoque:
        print("Erro: Código do produto já existe!")
        return
    
    nome = input("Digite o nome do produto: ")
    categoria = input("Digite a categoria (ex.: eletrônicos, vestuário): ")
    try:
        quantidade = int(input("Digite a quantidade em estoque: "))
        preco = float(input("Digite o preço: "))
    except ValueError:
        print("Erro: Quantidade e preço devem ser números!")
        return
    
    descricao = input("Digite a descrição do produto: ")
    fornecedor = input("Digite o fornecedor: ")
    
    estoque[codigo] = {
        "nome": nome,
        "categoria": categoria,
        "quantidade": quantidade,
        "preco": preco,
        "descricao": descricao,
        "fornecedor": fornecedor
    }
    salvar_estoque(estoque)
    print("Produto adicionado com sucesso!")

# Adiciona quantidade ao estoque
def adicionar_ao_estoque(estoque):
    print("\n=== Adicionar ao Estoque ===")
    codigo = input("Digite o código do produto: ")
    if codigo not in estoque:
        print("Erro: Produto não encontrado!")
        return
    
    try:
        quantidade = int(input("Digite a quantidade a adicionar: "))
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa!")
        estoque[codigo]["quantidade"] += quantidade
        salvar_estoque(estoque)
        print(f"Quantidade atualizada: {estoque[codigo]['quantidade']} unidades")
    except ValueError as e:
        print(f"Erro: {e}")

# Remove quantidade do estoque
def remover_do_estoque(estoque):
    print("\n=== Remover do Estoque ===")
    codigo = input("Digite o código do produto: ")
    if codigo not in estoque:
        print("Erro: Produto não encontrado!")
        return
    
    try:
        quantidade = int(input("Digite a quantidade a remover: "))
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa!")
        if quantidade > estoque[codigo]["quantidade"]:
            raise ValueError("Quantidade a remover excede o estoque!")
        estoque[codigo]["quantidade"] -= quantidade
        salvar_estoque(estoque)
        print(f"Quantidade atualizada: {estoque[codigo]['quantidade']} unidades")
    except ValueError as e:
        print(f"Erro: {e}")

# Atualiza manualmente a quantidade no estoque
def atualizar_estoque(estoque):
    print("\n=== Atualizar Estoque ===")
    codigo = input("Digite o código do produto: ")
    if codigo not in estoque:
        print("Erro: Produto não encontrado!")
        return
    
    try:
        quantidade = int(input("Digite a nova quantidade: "))
        if quantidade < 0:
            raise ValueError("Quantidade não pode ser negativa!")
        estoque[codigo]["quantidade"] = quantidade
        salvar_estoque(estoque)
        print(f"Quantidade atualizada: {estoque[codigo]['quantidade']} unidades")
    except ValueError as e:
        print(f"Erro: {e}")

# Verifica produtos com estoque baixo
def alerta_estoque_baixo(estoque, limite=5):
    print("\n=== Alerta de Estoque Baixo ===")
    encontrado = False
    for codigo, produto in estoque.items():
        if produto["quantidade"] <= limite:
            encontrado = True
            print(f"Alerta: {produto['nome']} (Código: {codigo}) - Estoque: {produto['quantidade']} unidades")
    if not encontrado:
        print("Nenhum produto com estoque baixo.")

# Exibe todos os produtos
def exibir_produtos(estoque):
    print("\n=== Lista de Produtos ===")
    if not estoque:
        print("Nenhum produto cadastrado.")
        return
    for codigo, produto in estoque.items():
        print(f"Código: {codigo}")
        print(f"Nome: {produto['nome']}")
        print(f"Categoria: {produto['categoria']}")
        print(f"Quantidade: {produto['quantidade']}")
        print(f"Preço: R${produto['preco']:.2f}")
        print(f"Descrição: {produto['descricao']}")
        print(f"Fornecedor: {produto['fornecedor']}")
        print("-" * 30)

# Menu principal
def menu():
    estoque = carregar_estoque()
    while True:
        print("\n=== Sistema de Gerenciamento de Estoque ===")
        print("1. Adicionar Produto")
        print("2. Adicionar ao Estoque")
        print("3. Remover do Estoque")
        print("4. Atualizar Estoque")
        print("5. Verificar Estoque Baixo")
        print("6. Exibir Produtos")
        print("7. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            adicionar_produto(estoque)
        elif opcao == "2":
            adicionar_ao_estoque(estoque)
        elif opcao == "3":
            remover_do_estoque(estoque)
        elif opcao == "4":
            atualizar_estoque(estoque)
        elif opcao == "5":
            alerta_estoque_baixo(estoque)
        elif opcao == "6":
            exibir_produtos(estoque)
        elif opcao == "7":
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o programa
if __name__ == "__main__":
    menu()