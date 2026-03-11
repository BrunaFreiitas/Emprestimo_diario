clientes = []
emprestimos = []
lucro_total = 0

while True:

    # CALCULAR VALOR TOTAL A RECEBER
    total_receber = 0
    ativos = 0

    for e in emprestimos:
        if e["saldo"] > 0:
            total_receber += e["saldo"]
            ativos += 1

    print("\n==============================")
    print("       DASHBOARD FINANCEIRO")
    print("==============================")
    print(f"Clientes cadastrados: {len(clientes)}")
    print(f"Empréstimos ativos: {ativos}")
    print(f"Valor total a receber: R$ {total_receber:.2f}")
    print(f"Lucro total em juros: R$ {lucro_total:.2f}")
    print("==============================\n")

    print("1 - Cadastrar cliente")
    print("2 - Novo empréstimo")
    print("3 - Registrar pagamento")
    print("4 - Ver empréstimos ativos")
    print("5 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":

        nome = input("Nome do cliente: ")
        cpf = input("CPF: ")

        clientes.append({
            "nome": nome,
            "cpf": cpf
        })

        print("Cliente cadastrado.")

    elif opcao == "2":

        cpf = input("CPF do cliente: ")

        cliente = None
        for c in clientes:
            if c["cpf"] == cpf:
                cliente = c

        if cliente is None:
            print("Cliente não encontrado.")
            continue

        valor = float(input("Valor emprestado: "))
        dias = int(input("Quantidade de parcelas: "))

        juros = valor * 0.30
        total = valor + juros
        parcela = total / dias

        emprestimos.append({
            "cpf": cpf,
            "valor": valor,
            "total": total,
            "parcela": parcela,
            "saldo": total,
            "dias": dias,
            "dia_atual": 1
        })

        lucro_total += juros

        print("Empréstimo registrado.")

    elif opcao == "3":

        cpf = input("CPF do cliente: ")

        for e in emprestimos:

            if e["cpf"] == cpf and e["saldo"] > 0:

                pago = input(f"Dia {e['dia_atual']} foi pago? (s/n): ")

                if pago.lower() == "s":

                    e["saldo"] -= e["parcela"]

                    if e["saldo"] < 0:
                        e["saldo"] = 0

                    print(f"Saldo restante: R$ {e['saldo']:.2f}")

                else:

                    e["dias"] += 2
                    print("⚠ Atraso detectado! +2 dias adicionados.")

                e["dia_atual"] += 1

    elif opcao == "4":

        print("\n=== EMPRÉSTIMOS ATIVOS ===")

        for e in emprestimos:

            if e["saldo"] > 0:

                print(f"CPF: {e['cpf']}")
                print(f"Saldo devedor: R$ {e['saldo']:.2f}")
                print(f"Parcela diária: R$ {e['parcela']:.2f}")
                print(f"Dia atual: {e['dia_atual']}")
                print("----------------------")

    elif opcao == "5":

        print("Sistema encerrado.")
        break
