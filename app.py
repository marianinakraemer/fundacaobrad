def exibir_menu():
    print("\n📘 Assistente Financeiro - Fundação Bradesco")
    print("Escolha uma opção:")
    print("1 - Simular investimento")
    print("2 - O que é CDB?")
    print("3 - O que é Poupança?")
    print("4 - O que é CDI?")
    print("5 - Ver último cálculo")
    print("0 - Sair")


def calcular_investimento(valor, meses):
    taxa = 0.01  # 1% ao mês (educacional)
    return valor * (1 + taxa) ** meses


def assistente():
    ultimo_calculo = None

    while True:
        exibir_menu()
        opcao = input("Digite a opção: ")

        # SAIR
        if opcao == "0":
            print("Assistente: Encerrando... Bons estudos! 📚")
            break

        # SIMULAÇÃO
        elif opcao == "1":
            try:
                valor = float(input("Digite o valor do investimento: R$ "))
                meses = int(input("Digite o tempo (em meses): "))

                if valor <= 0 or meses <= 0:
                    print("⚠️ Valores devem ser positivos.")
                    continue

                resultado = calcular_investimento(valor, meses)
                ultimo_calculo = resultado

                print(f"✅ Resultado: R$ {resultado:.2f}")
                print("💡 Este cálculo usa juros compostos de 1% ao mês (valor educacional).")

            except:
                print("⚠️ Entrada inválida. Tente novamente.")

        # CDB
        elif opcao == "2":
            print("📊 CDB (Certificado de Depósito Bancário):")
            print("É um investimento de renda fixa onde você empresta dinheiro ao banco e recebe juros sobre isso.")

        # POUPANÇA
        elif opcao == "3":
            print("💰 Poupança:")
            print("É um investimento seguro e simples, com rendimento mensal, indicado para iniciantes.")

        # CDI
        elif opcao == "4":
            print("📈 CDI (Certificado de Depósito Interbancário):")
            print("É uma taxa usada como referência para diversos investimentos como CDB.")

        # ÚLTIMO RESULTADO
        elif opcao == "5":
            if ultimo_calculo:
                print(f"📌 Último resultado: R$ {ultimo_calculo:.2f}")
            else:
                print("⚠️ Nenhum cálculo realizado ainda.")

        else:
            print("❌ Opção inválida. Escolha uma opção do menu.")


# EXECUTAR
assistente()
