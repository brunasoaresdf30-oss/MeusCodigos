#Meu site#
pacientes = []

def cadastrar_paciente():
    try:
        nome = input("Nome do paciente: ").strip()
        idade = int(input("Idade: "))
        telefone = input("Telefone: ")
        
        paciente = {"nome": nome, "idade": idade, "telefone": telefone}
        pacientes.append(paciente)
        print("Paciente cadastrado com sucesso!\n")
    except ValueError:
        print("Erro: Idade deve ser um número inteiro.\n")

def ver_estatisticas():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return

    total = len(pacientes)
    media_idade = sum(p["idade"] for p in pacientes) / total
    mais_novo = min(pacientes, key=lambda x: x["idade"])
    mais_velho = max(pacientes, key=lambda x: x["idade"])

    print(f"Total de pacientes: {total}")
    print(f"Idade média: {media_idade:.2f}")
    print(f"Paciente mais novo: {mais_novo['nome']} ({mais_novo['idade']} anos)")
    print(f"Paciente mais velho: {mais_velho['nome']} ({mais_velho['idade']} anos)\n")

def buscar_paciente():
    nome = input("Digite o nome do paciente: ").strip().lower()
    encontrados = [p for p in pacientes if p["nome"].lower() == nome]

    if encontrados:
        for p in encontrados:
            print(p)
    else:
        print("Paciente não encontrado.\n")

def listar_pacientes():
    if not pacientes:
        print("Nenhum paciente cadastrado.\n")
        return

    print("\n=== LISTA DE PACIENTES ===")
    for p in pacientes:
        print(f"Nome: {p['nome']} | Idade: {p['idade']} | Telefone: {p['telefone']}")
    print()

def menu():
    while True:
        print("=== SISTEMA CLÍNICA VIDA+ ===")
        print("1. Cadastrar paciente")
        print("2. Ver estatísticas")
        print("3. Buscar paciente")
        print("4. Listar todos os pacientes")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            cadastrar_paciente()
        elif opcao == "2":
            ver_estatisticas()
        elif opcao == "3":
            buscar_paciente()
        elif opcao == "4":
            listar_pacientes()
        elif opcao == "5":
            print("Saindo...")
            break
        else:
            print("Opção inválida!\n")

menu()
