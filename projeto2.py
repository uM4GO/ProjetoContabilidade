from datetime import datetime

# Lista para armazenar os lançamentos
lancamentos = []

def registrar_lancamento():
    print("\n--- Registrar Lançamento ---")

    while True:
        descricao = input("Digite a descrição do lançamento (ex: 'Salário', 'Compra supermercado'): ").strip()
        if descricao:
            break
        else:
            print("Descrição não pode ficar vazia.")

    while True:
        valor_str = input("Digite o valor do lançamento (ex: 100 ou 150.50): ").replace(",", ".")
        try:
            valor = float(valor_str)
            if valor <= 0:
                print("O valor deve ser maior que zero.")
                continue
            break
        except ValueError:
            print("Valor inválido. Digite um número válido (ex: 100 ou 150.50).")

    while True:
        tipo = input("Digite o tipo do lançamento ('entrada' ou 'saida'): ").strip().lower()
        if tipo in ["entrada", "saida"]:
            break
        else:
            print("Tipo inválido. Digite apenas 'entrada' ou 'saida'.")

    while True:
        data_str = input("Digite a data do lançamento no formato DD-MM-AAAA (ex: 10-03-2026): ").strip()
        try:
            data = datetime.strptime(data_str, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Data inválida. Use o formato DD-MM-AAAA (ex: 10-03-2026).")

    lancamento = {
        "descricao": descricao,
        "valor": valor,
        "tipo": tipo,
        "data": data
    }

    lancamentos.append(lancamento)
    print("Lançamento registrado com sucesso!\n")

def listar_lancamentos():
    print("\n--- Listar Lançamentos ---")

    if not lancamentos:
        print("Nenhum lançamento cadastrado.\n")
        return

    for i, l in enumerate(lancamentos, start=1):
        print(f"{i}. Data: {l['data'].strftime('%d-%m-%Y')} | Tipo: {l['tipo'].capitalize()} | Descrição: {l['descricao']} | Valor: R${l['valor']:.2f}")

    print("")

def consultar_saldo():
    print("\n--- Consultar Saldo ---")

    entradas = sum(l['valor'] for l in lancamentos if l['tipo'] == "entrada")
    saidas = sum(l['valor'] for l in lancamentos if l['tipo'] == "saida")
    saldo = entradas - saidas

    print(f"Total de Entradas: R${entradas:.2f}")
    print(f"Total de Saídas: R${saidas:.2f}")
    print(f"Saldo Atual: R${saldo:.2f}\n")

def filtrar_lancamentos():
    print("\n--- Filtrar Lançamentos ---")

    while True:
        tipo_filtro = input("Filtrar por tipo ('entrada', 'saida' ou 'todos'): ").strip().lower()
        if tipo_filtro in ["entrada", "saida", "todos"]:
            break
        else:
            print("Tipo inválido. Digite 'entrada', 'saida' ou 'todos'.")

    while True:
        data_inicio_str = input("Data inicial (DD-MM-AAAA) ou Enter para ignorar: ").strip()
        if data_inicio_str == "":
            data_inicio = None
            break
        try:
            data_inicio = datetime.strptime(data_inicio_str, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Data inválida. Use o formato DD-MM-AAAA.")

    while True:
        data_fim_str = input("Data final (DD-MM-AAAA) ou Enter para ignorar: ").strip()
        if data_fim_str == "":
            data_fim = None
            break
        try:
            data_fim = datetime.strptime(data_fim_str, "%d-%m-%Y").date()
            break
        except ValueError:
            print("Data inválida. Use o formato DD-MM-AAAA.")

    resultados = []

    for l in lancamentos:
        if tipo_filtro != "todos" and l['tipo'] != tipo_filtro:
            continue
        if data_inicio and l['data'] < data_inicio:
            continue
        if data_fim and l['data'] > data_fim:
            continue
        resultados.append(l)

    if not resultados:
        print("Nenhum lançamento encontrado com os filtros aplicados.\n")
        return

    print("\nLançamentos filtrados:")
    for i, l in enumerate(resultados, start=1):
        print(f"{i}. Data: {l['data'].strftime('%d-%m-%Y')} | Tipo: {l['tipo'].capitalize()} | Descrição: {l['descricao']} | Valor: R${l['valor']:.2f}")

    print("")


def menu():
    while True:
        print("--- Sistema Financeiro ---")
        print("1. Registrar lançamento")
        print("2. Listar lançamentos")
        print("3. Consultar saldo")
        print("4. Filtrar lançamentos")
        print("5. Sair")

        while True:
            escolha = input("Escolha uma opção (1-5): ").strip()
            if escolha in ["1", "2", "3", "4", "5"]:
                break
            else:
                print("Opção inválida. Digite um número de 1 a 5.")

        if escolha == "1":
            registrar_lancamento()
        elif escolha == "2":
            listar_lancamentos()
        elif escolha == "3":
            consultar_saldo()
        elif escolha == "4":
            filtrar_lancamentos()
        elif escolha == "5":
            print("Desligando o sistema...")
            break


if __name__ == "__main__":
    menu()