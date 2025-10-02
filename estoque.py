import json
import os

# Nome do arquivo onde os dados serão salvos
ARQUIVO = "estoque.json"

# -------- Funções de persistência --------
def carregar_estoque():
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def salvar_estoque():
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(estoque, f, indent=4, ensure_ascii=False)

# Carregar estoque do arquivo ao iniciar
estoque = carregar_estoque()

# -------- Funções principais --------
def cadastrar_produto():
    codigo = input("Digite o código do produto: ")
    if codigo in estoque:
        print("⚠️ Produto já cadastrado.")
        return
    
    nome = input("Digite o nome do produto: ")
    quantidade = int(input("Digite a quantidade inicial: "))
    local = input("Digite a localização (ex: Prateleira A1): ")
    
    estoque[codigo] = {"nome": nome, "quantidade": quantidade, "local": local}
    salvar_estoque()
    print(f"✅ Produto {nome} cadastrado com sucesso!")


def registrar_entrada():
    codigo = input("Digite o código do produto: ")
    if codigo in estoque:
        qtd = int(input("Digite a quantidade de entrada: "))
        estoque[codigo]["quantidade"] += qtd
        salvar_estoque()
        print("✅ Entrada registrada com sucesso.")
    else:
        print("⚠️ Produto não encontrado.")


def registrar_saida():
    codigo = input("Digite o código do produto: ")
    if codigo in estoque:
        qtd = int(input("Digite a quantidade de saída: "))
        if estoque[codigo]["quantidade"] >= qtd:
            estoque[codigo]["quantidade"] -= qtd
            salvar_estoque()
            print("✅ Saída registrada com sucesso.")
        else:
            print("⚠️ Estoque insuficiente.")
    else:
        print("⚠️ Produto não encontrado.")


def consultar_estoque():
    if not estoque:
        print("📦 Estoque vazio.")
        return
    
    print("\n📋 Estoque Atual:")
    for cod, dados in estoque.items():
        print(f"Código: {cod} | Nome: {dados['nome']} | "
            f"Quantidade: {dados['quantidade']} | Local: {dados['local']}")
        
        
def editar_produto():
    codigo = input("Digite o código do produto que deseja editar: ")
    if codigo in estoque:
        print(f"\n🔧 Editando produto: {estoque[codigo]['nome']}")
        novo_nome = input(f"Novo nome (atual: {estoque[codigo]['nome']}): ") or estoque[codigo]['nome']
        novo_qtd = input(f"Nova quantidade (atual: {estoque[codigo]['quantidade']}): ")
        novo_local = input(f"Novo local (atual: {estoque[codigo]['local']}): ") or estoque[codigo]['local']

        # Atualiza os valores
        estoque[codigo]['nome'] = novo_nome
        estoque[codigo]['quantidade'] = int(novo_qtd) if novo_qtd else estoque[codigo]['quantidade']
        estoque[codigo]['local'] = novo_local

        salvar_estoque()
        print(" Produto atualizado com sucesso!")
    else:
        print(" Produto não encontrado.")


# -------- MENU PRINCIPAL --------
def menu():
    while True:
        print("\n====== SISTEMA DE CONTROLE DE ESTOQUE ======")
        print("1 - Cadastrar Produto")
        print("2 - Registrar Entrada")
        print("3 - Registrar Saída")
        print("4 - Consultar Estoque")
        print("0 - Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            registrar_entrada()
        elif opcao == "3":
            registrar_saida()
        elif opcao == "4":
            consultar_estoque()
        elif opcao == "0":
            print("👋 Saindo do sistema...")
            break
        else:
            print("⚠️ Opção inválida, tente novamente.")

# Inicia o sistema
menu()
